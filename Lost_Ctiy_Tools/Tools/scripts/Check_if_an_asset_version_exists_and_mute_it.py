# Add New Layer
import loputils
import os
import re
from pxr import Sdf, Usd
node = hou.pwd()

# Call editableStage so the addSubLayer call will work
stage = node.editableStage()


usd_layer = hou.parm("usd_layer").evalAsString()
test = os.path.split(usd_layer)
path_dir = test[0]+"/"

prefix = path_dir+"_".join(test[-1].split(".")[0].split("_")[:-2])+"_"
extention = "."+test[-1].split(".")[-1]
pattern = r'v\d{2}_\d{3}'
dynamic_pattern = f'{re.escape(prefix)}{pattern}{re.escape(extention)}'


used_layers = stage.GetUsedLayers()

current_asset_version_exists = 0

list_of_layers_on_disk = []
for layer in used_layers:
    if os.path.exists(layer.identifier): 
        if re.match(dynamic_pattern, layer.identifier):
            list_of_layers_on_disk.append(layer.identifier)
            print("asset Layer Vserion Exists")
            if usd_layer == layer.identifier:
                current_asset_version_exists = 1
                print("the Current Asset Version Allredy Exists Pleas Export New Version")
                raise ValueError("Cant Export Asset Version That Allredy Exists")
            


        else:
            pass

            

layers_to_mute = " ".join(list_of_layers_on_disk)
print(layers_to_mute)


parm = hou.node("../Mute_Corect_Sublayers1/").parm("mutepaths")
parm.set(layers_to_mute)

