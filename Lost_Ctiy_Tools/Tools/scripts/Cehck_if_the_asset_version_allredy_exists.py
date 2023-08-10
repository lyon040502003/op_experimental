# Add New Layer
import loputils
import os
import re
from pxr import Sdf, Usd
node = hou.pwd()

version_parm = hou.node(node.parent().parent().path()).parm("Version")
inc_parm = hou.node(node.parent().parent().path()).parm("Increment")


print("test")
Asset_Version = version_parm.eval()
Asset_increment = inc_parm.eval()


usd_layer = hou.parm("usd_layer").evalAsString()
Asset_Container_File = hou.parm("asset_container_file").evalAsString()
test = os.path.split(usd_layer)
path_dir = test[0]+"/"


asset_save_foulder = os.path.split(usd_layer)[0]
asset_foulder_file_list = os.listdir(asset_save_foulder)
asset_foulder_file_list.sort()


current_asset_version_exists = 0

Asset_Sceene_info_massage = hou.node(node.parent().parent().path()).parm("labelparm7")

    
prefix = path_dir+"_".join(test[-1].split(".")[0].split("_")[:-2])+"_"

extention = "."+test[-1].split(".")[-1]
pattern = r'v\d{2}_\d{3}'
dynamic_pattern = f'{re.escape(prefix)}{pattern}{re.escape(extention)}'
            



higest_inc_version = 0
asset_name = "No Current Asset Version"
for files in asset_foulder_file_list:
    full_file_path = os.path.join(path_dir, files)


    if re.match(dynamic_pattern, full_file_path):
        print("found a version off the asset")
        print(files)
       
        
        if int(files.split(".")[0].split("_")[-1].lstrip('0')) > higest_inc_version:
            higest_inc_version = int(files.split(".")[0].split("_")[-1].lstrip('0'))
            asset_name = files
            

higest_inc_version = higest_inc_version +1

print(higest_inc_version)
Asset_Sceene_info_massage.set("Newest Curent Asset Version: {}".format(asset_name))
inc_parm.set(higest_inc_version)
