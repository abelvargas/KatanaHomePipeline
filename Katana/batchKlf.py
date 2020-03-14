### Loop through all alembic assets in a folder
### and export one .klf each with the alembic's name and a version.

import time
from Katana import Utils, Callbacks

#This script assumes all your alembic files live on the same folder. If that's not your case
#you will have to write your own function that loops through the directory and grabs the .abc
#files.
alembicPath = "C:/Users/abelv/Documents/Projetos/KB3D_IndustrialScifi/model.buildings/"
#Path to where you want to save the KLFs
klfPath = "C:/Users/abelv/Documents/Projetos/KB3D_IndustrialScifi/klf.buildings/"
#Simple version control. You can go all out and pick the latest version of the KLFs
#using another function.
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
    #Find first child of geo
    # Get the "name" parameter which is the root location of the alembic
    p = assetInNode.getParameter('name').getValue(0)
    geo = Nodes3DAPI.GetGeometryProducer(assetInNode, NodegraphAPI.GetCurrentGraphState())
    child = geo.getProducerByPath(p)
    rootLocationPath = child.getFirstChild().getFullName()
    #edit LookFileBake saveTo parameter and bake.
    lookFileBakeNode.getParameter("rootLocations").getChildByIndex(0).setValue(" ",0)
    lookFileBakeNode.getParameter("rootLocations").getChildByIndex(0).setValue(rootLocationPath,0)
    lookFileBakeNode.WriteToLookFile(None, str(klfPath+alembicFileName+klfVersion+".klf"))
