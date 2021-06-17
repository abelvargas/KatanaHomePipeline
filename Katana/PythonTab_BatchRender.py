### This script is a way to batch render from Katana's interactive mode ###
# Copy and paste this script into your python tab. Make sure to update RenderNode
# and frame range as noted below!

import NodegraphAPI
from Katana import KatanaFile
from Katana import RenderManager
def messageHandler( sequenceID, message ):
  print message

RenderNode = NodegraphAPI.GetNode('BG') # UPDATE with the name of your render node.
renderSettings = RenderManager.RenderingSettings()
renderSettings.frame=1001
renderSettings.mode=RenderManager.RenderModes.DISK_RENDER
renderSettings.asynchRenderMessageCB=messageHandler
renderSettings.asynch=False

for frame in range(1001, 1050): #UPDATE WITH YOUR FRAME RANGE!!!
    print '-' * 80
    print '\nRendering Node "%s" frame %s...' % (RenderNode.getName(), frame)
    renderSettings.frame = frame
    RenderManager.StartRender('diskRender', node=RenderNode, settings=renderSettings)
