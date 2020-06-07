from Katana import Nodes3DAPI
from Katana import NodegraphAPI
from Katana import ScenegraphManager

selectedGroups = ScenegraphManager.getActiveScenegraph().getSelectedLocations()
print selectedGroups[0]

t3d_grp = NodegraphAPI.CreateNode('Group', NodegraphAPI.GetRootNode())
t3d_grp.setName("T3Ds")
t3d_grp.addOutputPort('out')
t3d_grp_port = abc_grp.getReturnPort('out')

mergeNode = NodegraphAPI.CreateNode("Merge", t3d_grp)
mergeNode.setName('T3D_Merge')
mergeInputIndex = 0
mergePosition = NodegraphAPI.GetNodePosition(mergeNode)
xStartPos = mergePosition[0]
yStartPos = mergePosition[1]
XIncrementPosition = 0
print XIncrementPosition
xpos = xStartPos + XIncrementPosition
ypos = yStartPos + 50

for i in selectedGroups:
    merge_port = mergeNode.addInputPort('i'+str(mergeInputIndex))
    mergePosition = NodegraphAPI.GetNodePosition(mergeNode)

    t3d = NodegraphAPI.CreateNode("Transform3D", t3d_grp)
    t3d.getParameter("path").setValue(i,0)
    t3d.getParameter("makeInteractive").setValue("Yes",0)

    NodegraphAPI.SetNodePosition(t3d, [xpos,ypos])

    t3d.getOutputPort('out').connect(merge_port)
    mergeInputIndex += 1
    XIncrementPosition += 50
