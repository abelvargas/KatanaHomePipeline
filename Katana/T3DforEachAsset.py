from Katana import Nodes3DAPI
from Katana import NodegraphAPI
from Katana import ScenegraphManager

selectedGroups = ScenegraphManager.getActiveScenegraph().getSelectedLocations()
baseNode = NodegraphAPI.GetNode(NodegraphAPI.GetAllSelectedNodes()[0].getName())


for i in selectedGroups:

    y = 50
    previousNode = NodegraphAPI.GetNode(NodegraphAPI.GetAllSelectedNodes()[0].getName())
    previousNodePosition = NodegraphAPI.GetNodePosition(previousNode)
    xpos = previousNodePosition[0]
    ypos = previousNodePosition[1] - y
    t3d = NodegraphAPI.CreateNode("Transform3D", NodegraphAPI.GetRootNode())
    t3d.getParameter("path").setValue(i,0)
    t3d.getParameter("makeInteractive").setValue("Yes",0)
    NodegraphAPI.SetNodePosition(t3d, [xpos,ypos])
    try:
        previousNodePort = previousNode.getOutputPort('out')
        t3d.getInputPort('in').connect(previousNodePort)
    except:
        previousNodePort = previousNode.getOutputPort('default')
        t3d.getInputPort('in').connect(previousNodePort)
    NodegraphAPI.SetAllSelectedNodes('')
    NodegraphAPI.SetNodeSelected(t3d, True)
    y += 50
