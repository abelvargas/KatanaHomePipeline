#Import Alembic and klfFiles to Importomatic
#based on https://community.foundry.com/discuss/topic/152670/importing-alembic-and-look-file-into-project-with-importomatic#1201693
import os
alembicPath = "C:/Users/abelv/Documents/Projetos/KB3D_Highways/models.buildings/"
alembicFiles = []
for r, d, f in os.walk(alembicPath):
    for file in f:
        if ".abc" in file:
            alembicFiles.append(os.path.join(r, file))


klfPath = "C:/Users/abelv/Documents/Projetos/KB3D_Highways/klf.buildings/"
klfFiles = []
for r, d, f in os.walk(klfPath):
    for file in f:
        if ".klf" in file:
            klfFiles.append(os.path.join(r, file))


ImportomaticAPI = Plugins.ImportomaticAPI
KATANA_ROOT = os.getenv('KATANA_ROOT')
outputName = 'default'

impo_node = NodegraphAPI.CreateNode("Importomatic", NodegraphAPI.GetRootNode())
NodegraphAPI.SetNodeViewed(impo_node, True, True)
NodegraphAPI.SetNodeEdited(impo_node, True, True)

# Create alembic group node
for i in alembicFiles:
    alembicFileName = (i.split("/")[-1]).split(".")[-2]
    alembicNode = ImportomaticAPI.AssetModule.TriggerBatchCreateCallback('Alembic', impo_node, i, '')
    impo_node.insertNodeIntoOutputMerge(alembicNode, outputName)
    impo_node.layoutContents()
    klfMatch = [i for i in klfFiles if alembicFileName in i][0]
    alembicModule = ImportomaticAPI.AssetModule.GetHandlerForNode(alembicNode)
    alembicTreeRoot = alembicModule.getAssetTreeRoot(alembicNode)
    alembicTreeRoot.appendLookFile(klfMatch)
