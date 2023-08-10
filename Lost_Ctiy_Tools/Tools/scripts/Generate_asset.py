import os 
from pxr import Usd

parent_foulder = hou.parm("parent_foulder").evalAsString()
asset_sceene_name = hou.parm("asset_sceene_name").evalAsString()
asset_name = hou.parm("asset_name").evalAsString()

master_foulder_appendy = "_ASSET_SCEENE"
shoop_container_appendy = "_SHOOP_CONTAINER"
shoop_sceene_appendy = "_SHOOP_v"
asset_shop_foulder_name = "Asset_Shop"

asset_foulder_appendy = "_ASSET"
asset_Container_appendy = "_ASSET_CONTAINER"

# generate paths 
asset_sceene_foulder_path = os.path.join( parent_foulder, (asset_sceene_name + master_foulder_appendy))
Asset_Shop_path = os.path.join( asset_sceene_foulder_path, asset_shop_foulder_name)


# asset infos
asset_foulder = os.path.join(Asset_Shop_path, (asset_name + asset_foulder_appendy))
asset_container = os.path.join(asset_foulder, (asset_name + asset_Container_appendy + ".usd"))

asset_foulder_msci = os.path.join(asset_foulder, "msci")
asset_foulder_etc = os.path.join(asset_foulder, "etc")
asset_foulder_geo = os.path.join(asset_foulder, "geo")

print(asset_container)

try:
    os.mkdir(asset_foulder)
    
    os.mkdir(asset_foulder_msci)
    os.mkdir(asset_foulder_etc)
    os.mkdir(asset_foulder_geo)
    
    Usd.Stage.CreateNew(asset_container)
except:
    print("asset allredy exists ")

