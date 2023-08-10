import os 
from pxr import Usd
import re

node = hou.pwd()

parent_foulder = hou.parm("parent_foulder").evalAsString()
asset_sceene_name = hou.parm("asset_sceene_name").evalAsString()
sceeme_version = hou.parm("sceene_version").eval()

master_foulder_appendy = "_ASSET_SCEENE"
shoop_container_appendy = "_SHOOP_CONTAINER"
shoop_sceene_appendy = "_SHOOP_v"

version_number_padded = f'{sceeme_version:02}'


# generate paths 
asset_sceene_foulder_path = os.path.join( parent_foulder, (asset_sceene_name + master_foulder_appendy))

asset_sceene_path = os.path.join( asset_sceene_foulder_path, (asset_sceene_name + shoop_sceene_appendy))

prefix = os.path.join(asset_sceene_foulder_path, (asset_sceene_name + shoop_sceene_appendy + version_number_padded))
extention = ".usd"
pattern = r'_\d{3}'
dynamic_pattern = f'{re.escape(prefix)}{pattern}{re.escape(extention)}'


files_in_sceene_dir = os.listdir(asset_sceene_foulder_path) 

found_file = 0
higest_inc = 1


for file in files_in_sceene_dir:
    if re.match(dynamic_pattern, os.path.join(asset_sceene_foulder_path, file)):
        found_file = 1
        higest_inc = int(file.split(".")[0].split("_")[-1].lstrip('0'))
        higest_inc = higest_inc +1
        
        


inc_number_padded = f'{higest_inc:03}'



file_to_generate = os.path.join(asset_sceene_foulder_path, (asset_sceene_name + shoop_sceene_appendy + version_number_padded + "_" + inc_number_padded + ".usd"))

# Creating the sceene file 
Usd.Stage.CreateNew(file_to_generate)

