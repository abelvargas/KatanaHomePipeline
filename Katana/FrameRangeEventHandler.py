#https://community.foundry.com/discuss/topic/108691/graph-state-variable?mode=Post&postID=927145&show=set%2cframe%2crange#927145
#Assumes there's a node called "Shot_InOut" that has the user attributes for
#each shot, in and out times.
#This prints on the shell so look at it for clues, not the Python window in Katana
def MyEventHandler(eventType, eventID, node, param):
    if node is not NodegraphAPI.GetRootNode():
        return

    if param.getFullName(includeNodeName=False) == 'variables.Shot.value':
        if param.getValue(0) == "Shot01":
            NodegraphAPI.GetNode('rootNode').getParameter('inTime').setValue(NodegraphAPI.GetNode('Shot_InOut').getParameter('user.Shot01.In').getValue(0),0)
            NodegraphAPI.GetNode('rootNode').getParameter('outTime').setValue(NodegraphAPI.GetNode('Shot_InOut').getParameter('user.Shot01.Out').getValue(0),0)
        if param.getValue(0) == "Shot02":
            NodegraphAPI.GetNode('rootNode').getParameter('inTime').setValue(NodegraphAPI.GetNode('Shot_InOut').getParameter('user.Shot02.In').getValue(0),0)
            NodegraphAPI.GetNode('rootNode').getParameter('outTime').setValue(NodegraphAPI.GetNode('Shot_InOut').getParameter('user.Shot02.Out').getValue(0),0)
        if param.getValue(0) == "Shot03":
            NodegraphAPI.GetNode('rootNode').getParameter('inTime').setValue(NodegraphAPI.GetNode('Shot_InOut').getParameter('user.Shot03.In').getValue(0),0)
            NodegraphAPI.GetNode('rootNode').getParameter('outTime').setValue(NodegraphAPI.GetNode('Shot_InOut').getParameter('user.Shot03.Out').getValue(0),0)
        if param.getValue(0) == "Shot04":
            NodegraphAPI.GetNode('rootNode').getParameter('inTime').setValue(NodegraphAPI.GetNode('Shot_InOut').getParameter('user.Shot04.In').getValue(0),0)
            NodegraphAPI.GetNode('rootNode').getParameter('outTime').setValue(NodegraphAPI.GetNode('Shot_InOut').getParameter('user.Shot04.Out').getValue(0),0)

Utils.EventModule.RegisterEventHandler(MyEventHandler, "parameter_finalizeValue")
