###Attempting to render in a loop###
#all very messy right now. AND NOT WORKING

import os
###BIG RENDER LOOP###
##List Assets in a folder
alembicPath = "C:/Users/abelv/Documents/Projetos/KB3D_Highways/model.buildings/"
scriptPath = "C:/Users/abelv/Documents/Projetos/KB3D_Highways/lookdev.buildings/KB3D_HWY_loodev_02.katana"
renderVersion = "_01"
katanaPath = "C:/Program Files/Katana3.6v1/bin/"
#Get alembic files in alembicDir includins directory path
alembicFiles = []
# r=root, d=directories, f = files
for r, d, f in os.walk(alembicPath):
    for file in f:
        if '.abc' in file:
            alembicFiles.append(os.path.join(r, file))
#Part 1 - Sript mode to change AlembicIn asset and renderPath based on asset name, save.
#Launch Katana Script
cmd = [katanaPath+"katanaBin.exe --shell"]
import subprocess
p = subprocess.Popen([
    cmd,
    'KatanaFile.Load("C:/Users/abelv/Documents/Projetos/KB3D_Highways/lookdev.buildings/KB3D_HWY_loodev_02.katana")',
    'assetInNode = NodegraphAPI.GetNode("ASSET_IN")', 'print assetInNode.getParameter("abcAsset").getValue(1)'],
    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout:
    print line
p.wait()
print p.returncode

#Get ASSET_IN
assetInNode = NodegraphAPI.GetNode("ASSET_IN")

###Loop all alembics and generate one klf for each.
for alembic in alembicFiles:
    #edit abcAsset parameter in ASSET_IN
    assetInNode.getParameter("abcAsset").setValue(alembic,0)
    #file name without extention
    alembicFileName = (alembic.split("/")[-1]).split(".")[0]
#Part 2 - Create Batch

import NodegraphAPI
from Katana import KatanaFile
from Katana import RenderManager
def messageHandler( sequenceID, message ):
  print message

RenderNode = NodegraphAPI.GetNode('Render') # Getting Render node
renderSettings = RenderManager.RenderingSettings()
renderSettings.frame=1
renderSettings.mode=RenderManager.RenderModes.DISK_RENDER
renderSettings.asynchRenderMessageCB=messageHandler
renderSettings.asynch=False
RenderManager.StartRender('diskRender', node=RenderNode, settings=renderSettings)
