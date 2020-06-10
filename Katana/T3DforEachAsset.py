#This script will create a Transform3D for each location selected in the
#scenegraph below the selected node.
import sys
from Katana import Nodes3DAPI
from Katana import NodegraphAPI
from Katana import ScenegraphManager
#Get scenegraph seletion.
selectedGroups = ScenegraphManager.getActiveScenegraph().getSelectedLocations()
#Get seleted node
try:
    baseNode = NodegraphAPI.GetNode(NodegraphAPI.GetAllSelectedNodes()[0].getName())
except:
    sys.exit("Select a node on the nodegraph")

for i in selectedGroups:
    y = 50 #inital node position on nodegraph
    try:
        previousNode = NodegraphAPI.GetNode(NodegraphAPI.GetAllSelectedNodes()[0].getName())
    except IndexError:
        break
    previousNodePosition = NodegraphAPI.GetNodePosition(previousNode)
    xpos = previousNodePosition[0]
    ypos = previousNodePosition[1] - y
    t3d = NodegraphAPI.CreateNode("Transform3D", NodegraphAPI.GetRootNode())
    t3d.getParameter("path").setValue(i,0)
    t3d.getParameter("makeInteractive").setValue("Yes",0)
    NodegraphAPI.SetNodePosition(t3d, [xpos,ypos])
    #ports change names so trying more than one.
    try:
        previousNodePort = previousNode.getOutputPort('out')
        t3d.getInputPort('in').connect(previousNodePort)
    except:
        previousNodePort = previousNode.getOutputPort('default')
        t3d.getInputPort('in').connect(previousNodePort)
    NodegraphAPI.SetAllSelectedNodes('')
    NodegraphAPI.SetNodeSelected(t3d, True)
    y += 50 #adding space for next node in loop
