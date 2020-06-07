#creates one importomatic with all alembics in a folder.
#based on the link below
#https://community.foundry.com/discuss/post/1103740
import os
##List Assets in a folder
alembicPath = "C:/Users/abelv/Documents/Projetos/KB3D_Highways/models.buildings/"
#Get alembic files in alembicDir includins directory path
alembicFiles = []
for r, d, f in os.walk(alembicPath):
    for file in f:
        if '.abc' in file:
            alembicFiles.append(os.path.join(r, file))
            #print i
###
# Add Alembic to Importomatic
###
impo_node = NodegraphAPI.CreateNode("Importomatic", NodegraphAPI.GetRootNode())

# Create alembic group node

for i in alembicFiles:
    alembicFileName = (i.split("/")[-1]).split(".")[-2]
    abc_grp = NodegraphAPI.CreateNode('Group', NodegraphAPI.GetRootNode())
    abc_grp.setName(alembicFileName)
    abc_grp.setType('Alembic')
    abc_grp.addOutputPort('out')
    abc_grp_port = abc_grp.getReturnPort('out')

# Build group node params for importomatic
    assetinfo_page = abc_grp.getParameters().createChildGroup('assetInfo')

# Create alembic_in node
    abc_path = i
    abc_in_node = NodegraphAPI.CreateNode('Alembic_In', abc_grp)
    abc_in_node.setName(alembicFileName)
    abc_in_node.getParameter('abcAsset').setValue(abc_path, 0)
    abc_in_node.getParameter('name').setValue("/root/world/geo", 0)
    abc_node_port = abc_in_node.getOutputPort('out')

    # Connect ports
    abc_node_port.connect(abc_grp_port)

    # Add to importomatic
    impo_node.insertNodeIntoOutputMerge(abc_grp, 'default') # (node, importomatic output name)
