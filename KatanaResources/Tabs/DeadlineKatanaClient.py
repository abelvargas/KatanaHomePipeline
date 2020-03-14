"""
NAME: Submit to Deadline
ICON: logo.png
DROP_TYPES:
SCOPE:
Submit Scene To Deadline

"""

# The following symbols are added when run as shelf buttons:
# exit():      Allows 'error-free' early exit from the script.
# dropEvent:   If your script registers DROP_TYPES, this is a QDropEvent
#              upon a valid drop. Otherwise, it is None.
#              Example:  Registering for "nodegraph/nodes" DROP_TYPES
#                        allows the user to get dropped nodes using
#       nodes = [NodegraphAPI.GetNode(x) for x in
#               str(dropEvent.encodedData( 'nodegraph/nodes' )).split(',')]
# console_print(message, raisePanel = False):
#              If the Python Console exists, print the message to it.
#              Otherwise, print the message to the shell. If raisePanel
#              is passed as True, the panel will be raised to the front.
from __future__ import print_function
from Katana import QtCore, QtGui, UI4

import sys
import os
import subprocess
import traceback

class DeadlineTab(UI4.Tabs.BaseTab):

    def __init__(self, parent):
        UI4.Tabs.BaseTab.__init__(self, parent)
        RunSubmitter(self)

def GetDeadlineCommand():
    deadlineBin = ""
    try:
        deadlineBin = os.environ['DEADLINE_PATH']
    except KeyError:
        #if the error is a key error it means that DEADLINE_PATH is not set. however Deadline command may be in the PATH or on OSX it could be in the file /Users/Shared/Thinkbox/DEADLINE_PATH
        pass
        
    # On OSX, we look for the DEADLINE_PATH file if the environment variable does not exist.
    if deadlineBin == "" and  os.path.exists( "/Users/Shared/Thinkbox/DEADLINE_PATH" ):
        with open( "/Users/Shared/Thinkbox/DEADLINE_PATH" ) as f:
            deadlineBin = f.read().strip()

    deadlineCommand = os.path.join(deadlineBin, "deadlinecommand")
    
    return deadlineCommand
        
def GetRepositoryPath(subdir = None):
    deadlineCommand = GetDeadlineCommand()
    
    startupinfo = None
    if os.name == 'nt':
        # Python 2.6 has subprocess.STARTF_USESHOWWINDOW, and Python 2.7 has subprocess._subprocess.STARTF_USESHOWWINDOW, so check for both.
        if hasattr( subprocess, '_subprocess' ) and hasattr( subprocess._subprocess, 'STARTF_USESHOWWINDOW' ):
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess._subprocess.STARTF_USESHOWWINDOW
        elif hasattr( subprocess, 'STARTF_USESHOWWINDOW' ):
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    
    args = [deadlineCommand, "-GetRepositoryPath "]
    if subdir != None and subdir != "":
        args.append(subdir)

    proc = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=startupinfo)
    path, errors = proc.communicate()
    path = path.replace("\n","").replace("\r","")
    
    return path

def RunSubmitter(katanaTabReference):
    path = GetRepositoryPath("submission/Katana/Main")
    print( "-----" )
    print( path )
    print( "-----" )
    if path != "":
        path = path.replace( "\\", "/" )
        
        # Add the path to the system path
        if path not in sys.path :
            print( "Appending \"" + path + "\" to system path to import SubmitKatanaToDeadline module" )
            sys.path.append( path )
        else:
            print( "\"%s\" is already in the system path" % path )

        # Import the script and call the main() function
        try:
            import SubmitKatanaToDeadline
            print( "Populating Katana Submitter..." )
            SubmitKatanaToDeadline.PopulateSubmitter(katanaTabReference) # The pointer to the tab is sent to the submission script to be populated 
        except:
            print( traceback.format_exc() )
            print( "An error occured while attempting to launch SubmitKatanaToDeadline.py. Please make sure that the Deadline Client has been installed on this machine, that the Deadline Client bin folder is set in the DEADLINE_PATH environment variable, and that the Deadline Client has been configured to point to a valid Repository." )
    else:
        print( "The SubmitKatanaToDeadline.py script could not be found in the Deadline Repository. Please make sure that the Deadline Client has been installed on this machine, that the Deadline Client bin folder is set in the DEADLINE_PATH environment variable, and that the Deadline Client has been configured to point to a valid Repository." )

#DEBUG only (comment next line out when not debugging)
#RunSubmitter(DeadlineTab)

PluginRegistry = [
    ('KatanaPanel', 2.0, 'Thinkbox/Submit To Deadline', DeadlineTab),
]
