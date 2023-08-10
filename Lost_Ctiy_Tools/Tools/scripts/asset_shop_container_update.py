# Add New Layer
import loputils
import os
import re
from pxr import Sdf, Usd
node = hou.pwd()
# Call editableStage so the addSubLayer call will work
#stage = node.editableStage()

Asset_Sceene_info_massage = hou.node(node.parent().parent().path()).parm("labelparm6")


asset_shoop_Container_path = hou.parm("Asset_Shoop_container_path").evalAsString()
usd_layer = hou.parm("usd_layer").evalAsString()


test = os.path.split(usd_layer)
path_dir = test[0]+"/"

prefix = path_dir+"_".join(test[-1].split(".")[0].split("_")[:-2])+"_"
extention = "."+test[-1].split(".")[-1]
pattern = r'v\d{2}_\d{3}'
dynamic_pattern = f'{re.escape(prefix)}{pattern}{re.escape(extention)}'





asset_shop_container_stage = Usd.Stage.Open(asset_shoop_Container_path)
asset_shop_container_stage_dir = os.path.dirname(asset_shoop_Container_path)
os.chdir(asset_shop_container_stage_dir)
sublayers = asset_shop_container_stage.GetRootLayer().subLayerPaths

layer_version_exists = 0

top_lvl_info_txt = ""

layer_exists = 0

if os.path.exists(usd_layer):
    print("Shop File Exists and can be added")

    for layer in sublayers:
    
        if re.match(dynamic_pattern, os.path.abspath(layer)):
            print("layer Version Allredy Exists")
            layer_exists = 1
            
            if asset_shoop_Container_path == os.path.abspath(layer):
                print(" the curent version is the version you want to add")
                top_lvl_info_txt = "the curent selected version is allredy added"
                
            else: 
                print(" the curent version is a diverent one from the one you want to add")
                print(" add selected version now")
                sublayers.remove(layer)
                rel_path_to_layer_file = os.path.relpath(usd_layer)
                sublayers.append(rel_path_to_layer_file)
                top_lvl_info_txt = "there is a subler version that diverent form the selected one will replace"
        
        else:
            print("this layer is not a version off the layer ")
    if not layer_exists:
        print(layer_exists)
        print("there is no matching subler will add subler now")
        rel_path_to_layer_file = os.path.relpath(usd_layer)
        sublayers.append(rel_path_to_layer_file)
        top_lvl_info_txt = " no sublayer in file will add now"
                    

            
else: 
    print("file dosnt exist on disk")
    top_lvl_info_txt = " the selected file is not on disk pleas create "
    


asset_shop_container_stage.GetRootLayer().Save()


Asset_Sceene_info_massage.set(top_lvl_info_txt)
