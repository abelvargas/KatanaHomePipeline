### Loop through all alembic assets in a folder
### and export one .klf each with the alembic's name and a version.

import time
from Katana import Utils, Callbacks


#Change the path to your own. First where the Alembics are, then where to save the KLFs
alembicPath = "C:/Users/abelv/Documents/Projetos/KB3D_IndustrialScifi/model.buildings/"
klfPath = "C:/Users/abelv/Documents/Projetos/KB3D_IndustrialScifi/klf.buildings/"
klfVersion = "_03"

#Get alembic files in alembicDir includins directory path
alembicFiles = []
# r=root, d=directories, f = files
for r, d, f in os.walk(alembicPath):
    for file in f:
        if '.abc' in file:
            alembicFiles.append(os.path.join(r, file))

#Get LookFileBake and ASSET_IN
lookFileBakeNode = NodegraphAPI.GetNode("LookFileBake")
assetInNode = NodegraphAPI.GetNode("ASSET_IN")

###Loop all alembics and generate one klf for each.
for alembic in alembicFiles:
    #edit abcAsset parameter in ASSET_IN
    assetInNode.getParameter("abcAsset").setValue(alembic,0)
    #file name without extention
    alembicFileName = (alembic.split("/")[-1]).split(".")[0]
    time.sleep(1)
    #Find first child of geo with _grp on the name
    Utils.EventModule.ProcessAllEvents() #refresh widget
    collector = Widgets.CollectAndSelectInScenegraph('//*_grp', "/root/world/geo")
    time.sleep(1)
    rootLocationPath = collector.collectAndSelect(select=True, replace=True, node=node)[0]
    print(rootLocationPath)
    #edit LookFileBake saveTo parameter and bake.
    lookFileBakeNode.getParameter("rootLocations").getChildByIndex(0).setValue(" ",0)
    lookFileBakeNode.getParameter("rootLocations").getChildByIndex(0).setValue(rootLocationPath,0)
    lookFileBakeNode.WriteToLookFile(None, str(klfPath+alembicFileName+klfVersion+".klf"))
