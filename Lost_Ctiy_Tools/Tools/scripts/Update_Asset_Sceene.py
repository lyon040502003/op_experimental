# Add New Layer
import loputils
import os
import re
from pxr import Usd
from pprint import pprint
node = hou.pwd()

print("this")
# Call editableStage so the addSubLayer call will work
#stage = node.editableStage()

usd_layer = hou.parm("Asset_Container_path").evalAsString()
shoop_sceene_path = hou.parm("Shoop_sceene_file_path").evalAsString()

asset_shop_stage = Usd.Stage.Open(shoop_sceene_path)
asset_shop_stage_dir = os.path.dirname(shoop_sceene_path)

os.chdir(asset_shop_stage_dir)
asset_sublayers = asset_shop_stage.GetRootLayer().subLayerPaths
asset_sublayers_abs_path = []



for layer in asset_sublayers:
    asset_sublayers_abs_path.append(os.path.abspath(layer))
    
    
if usd_layer in asset_sublayers_abs_path:
    print("Asset Container Was allredy added to the Asset Sceene")
else:
    print("Asset Continer not yet added to the Asset Sceene")
    rel_asset_container_path = "./" + os.path.relpath(usd_layer)
    print(rel_asset_container_path)
    asset_shop_stage.GetRootLayer().subLayerPaths.append(rel_asset_container_path)
    asset_shop_stage.GetRootLayer().Save()

    
   

