import os 
from pxr import Usd


main_container_path = hou.parm("main_container").evalAsString()
sceene_container_path = hou.parm("Sceene_container").evalAsString()

main_container = Usd.Stage.Open(main_container_path)


# check if sceene container allredy exists 

os.chdir(os.path.dirname(main_container_path))
if sceene_container_path in [os.path.abspath(files) for files in main_container.GetRootLayer().subLayerPaths]:
	print("the sceene container is allredy added to the main container")
	print(main_container.GetRootLayer().subLayerPaths)
	
else:
	print("the sceene container was not yet added to the main container")
	main_container.GetRootLayer().subLayerPaths.append(os.path.relpath(sceene_container_path))
	main_container.Save()
