#This script exports to an alembic file anything selected on the outliner
#It also creates an attribute in the allembic to be used in other DCCs,
#in this case, my previously created materialName attribute
import maya.cmds as cmd

selected = cmds.ls(sl=True,long=True)
start = 1
end = 1
attributeName = "materialName"
#Choose your own path HERE
projectPath = "C:/Users/abelv/Documents/Projetos/KB3D_Warzone/models.buildings/KB3D_WRZ_"
for i in selected:
    root ="-root "+str(i)
    save_name = projectPath+i[1:-4]+".abc"
    command = "-frameRange " + str(start) + " " + str(end) +" -attr " + attributeName + " -uvWrite -worldSpace " + root + " -file " + save_name
    cmd.AbcExport ( j = command )
