### Loop through all alembic assets in a folder
### and export one .klf each with the alembic's name and a version.

import time
from Katana import Utils, Callbacks

alembicPath = "C:/Users/abelv/Documents/Projetos/KB3D_Highways/models.buildings/"
klfPath = "C:/Users/abelv/Documents/Projetos/KB3D_Highways/klf.buildings/"
klfVersion = "_01"

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
    # Get the "name" parameter which is the root location of the alembic
    assetInNode.getParameter('name').setValue("/root/world/geo/"+alembicFileName,0)
    assetInName = assetInNode.getParameter('name').getValue(0)
    Utils.EventModule.ProcessAllEvents()
    time.sleep(0.1)
    rootLocationPath = assetInName
    #edit LookFileBake saveTo parameter and bake.
    lookFileBakeNode.getParameter("rootLocations").getChildByIndex(0).setValue(" ",0)
    lookFileBakeNode.getParameter("rootLocations").getChildByIndex(0).setValue(rootLocationPath,0)
    lookFileBakeNode.WriteToLookFile(None, str(klfPath+alembicFileName+klfVersion+".klf"))
