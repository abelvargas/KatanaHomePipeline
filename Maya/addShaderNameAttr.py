#This script adds a string attribute to each shape of you maya scene containing
#it's shader's name. I use this to automate shader assignment in Katana and drive
#some collections.

import maya.cmds as mc

#This line selects all shapes in you script
selectShape=mc.select(mc.listRelatives(mc.ls(geometry=True), p=True, path=True), r=True)
#List all selected shapes
listSelected= mc.ls (sl=True, dag=True, leaf=True)
#Name your attribute
newAttr = "materialName"

#Loops through all items in the list, creates the attribute of type string
#gets the shader name assigned to the shape and places it in the new attribute
for i in listSelected:
    shadeEng = mc.listConnections(i, type="shadingEngine")
    #In my case, I needed to remove the first 2 letters and last 2
    #so I pick the range I want to use with the [3:-2].
    shaderName = str(mc.ls(mc.listConnections(shadeEng ), materials = True))[3:-2]
    mc.addAttr (i, ln=newAttr, dt="string")
    #You may choose to not lock the attribute and make it keyable
    #depending on your needs
    mc.setAttr(i+"."+newAttr, shaderName, type="string",e=True, keyable=False, lock=True)
