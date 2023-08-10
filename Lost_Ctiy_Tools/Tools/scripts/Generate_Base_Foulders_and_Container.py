import os 
from pxr import Usd

parent_foulder = hou.parm("parent_foulder").evalAsString()
asset_sceene_name = hou.parm("asset_sceene_name").evalAsString()

master_foulder_appendy = "_ASSET_SCEENE"
shoop_container_appendy = "_SHOOP_CONTAINER"
shoop_sceene_appendy = "_SHOOP_v"

asset_shop_foulder_name = "Asset_Shop"


# generate paths 
asset_sceene_foulder_path = os.path.join( parent_foulder, (asset_sceene_name + master_foulder_appendy))
Asset_Shop_path = os.path.join( asset_sceene_foulder_path, asset_shop_foulder_name)

# generate base files 

asset_sceene_container_path = os.path.join(asset_sceene_foulder_path, (asset_sceene_name + shoop_container_appendy + ".usd"))


# print the generation paths 
print("-"*80)
print("generating the following files and paths")
print(asset_sceene_foulder_path)
print(Asset_Shop_path)
print(asset_sceene_container_path)
print("-"*80)
print()


try:
    os.mkdir(asset_sceene_foulder_path)
    os.mkdir(Asset_Shop_path)
    Usd.Stage.CreateNew(asset_sceene_container_path)

except:
    print("the foulders allredy exist")

