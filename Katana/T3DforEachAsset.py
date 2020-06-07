from Katana import Nodes3DAPI
from Katana import NodegraphAPI
from Katana import ScenegraphManager

selectedGroups = ScenegraphManager.getActiveScenegraph().getSelectedLocations()
baseNode = NodegraphAPI.GetNode(NodegraphAPI.GetAllSelectedNodes()[0].getName())
nodePosition = NodegraphAPI.GetNodePosition(baseNode)

x = 0
y = 50
xpos = nodePosition[0] + x
ypos = nodePosition[1] - y

dot = NodegraphAPI.CreateNode("Dot", NodegraphAPI.GetRootNode())
NodegraphAPI.SetNodePosition(dot, [xpos,ypos])
y += 50
dot.getInputPort('input').connect(baseNode.getOutputPort('default'))
dot.setName("T3D_dot")
dot.addOutputPort("out")
NodegraphAPI.SetAllSelectedNodes('')
NodegraphAPI.SetNodeSelected(dot, True)


for i in selectedGroups:

    y = 50
    previousNode = NodegraphAPI.GetNode(NodegraphAPI.GetAllSelectedNodes()[0].getName())
    previousNodePosition = NodegraphAPI.GetNodePosition(previousNode)
    xpos = previousNodePosition[0]
    ypos = previousNodePosition[1] - y
    previousNodePort = previousNode.getOutputPort('out')
    t3d = NodegraphAPI.CreateNode("Transform3D", NodegraphAPI.GetRootNode())
    t3d.getParameter("path").setValue(i,0)
    t3d.getParameter("makeInteractive").setValue("Yes",0)
    NodegraphAPI.SetNodePosition(t3d, [xpos,ypos])
    t3d.getInputPort('in').connect(previousNodePort)
    NodegraphAPI.SetAllSelectedNodes('')
    NodegraphAPI.SetNodeSelected(t3d, True)
    y += 50
