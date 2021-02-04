#This script switches all paths to an expression leading to the same result but works on any system.

#Get all nodes of a certain type.
for i in NodegraphAPI.GetAllNodesByType("UsdShadingNode", includeDeleted=False, sortByName=True):
    nodeName = i.getParameter('name').getValue(0)
    node = NodegraphAPI.GetNode(nodeName)

    #Find the current path and ignore nodes without this parameter.
    if node.getParameter('parameters.file.value') == None:
        pass
    elif "macbeth" in node.getParameter('parameters.file.value').getValue(0):
        pass
    else:
        longPath = node.getParameter('parameters.file.value').getValue(0)
    
        #Create new path.
        shortPath = longPath.replace('E:/AAA_KWS_Ashli_Light/', '')
        expressionPath = str("project.dir" + "+'/../'+"+"\'"+shortPath+"\'")

        #set node file path to expression with the correct project.dir replacement
        node.getParameter('parameters.file.value').setExpression(expressionPath, True)
