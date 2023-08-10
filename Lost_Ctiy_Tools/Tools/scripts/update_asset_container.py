# Add New Layer
import loputils
import os
import re
from pxr import Sdf, Usd



container_file = hou.parm("container_file").evalAsString()
# Call editableStage so the addSubLayer call will work
stage = Usd.Stage.Open(container_file)


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
                print("the Current Asset Version Allredy Exists Pleas Export New Version")
                current_asset_version_exists = 1


        else:
            pass

            

if not current_asset_version_exists: # no version off the asset was added
	print("no current version off the asset was found")
	if len(list_of_layers_on_disk) != 0: # check if there is a versoin off the asset 
		print(" no version off the asset was found")
		for layer in list_of_layers_on_disk:
			stage.GetRootLayer().subLayerPaths.remove(layer) # make shure that no version off the asset exist on the container file 
		
stage.GetRootLayer().subLayerPaths.append(usd_layer)
stage.Save()
	
	
