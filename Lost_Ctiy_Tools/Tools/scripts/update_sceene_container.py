import os
from pxr import Usd
import re

sceene_container_path = asset_sceene_name = hou.parm("sceene_container_path").evalAsString()
Sceene_path = asset_sceene_name = hou.parm("work_sceene").evalAsString()

sceene_container_stage = Usd.Stage.Open(sceene_container_path)

sceene_container_stage_sublayers = sceene_container_stage.GetRootLayer().subLayerPaths

os.chdir(os.path.dirname(sceene_container_path))


prefix = os.path.join(os.path.split(Sceene_path)[0],os.path.split(Sceene_path)[-1][:-10])

extention = ".usd"
pattern = r'\d{2}_\d{3}'
dynamic_pattern = f'{re.escape(prefix)}{pattern}{re.escape(extention)}'




if len(sceene_container_stage_sublayers) == 0:
	print("this container has no sceenes added will add sceene now")
	print(os.path.relpath(Sceene_path))
	sceene_container_stage_sublayers.append("./"+os.path.relpath(Sceene_path))
	sceene_container_stage.Save()
else:
	
	for path in sceene_container_stage_sublayers:

		if Sceene_path == os.path.abspath(path):
			print("Sceene Was allredy added ")
			print(os.path.abspath(path))
		else:
			print("this version off the sceene is not yet added")
			
			if re.match(dynamic_pattern, os.path.abspath(path)):
				print("there is a version off the sceene added to the container")
				print(os.path.abspath(path))
				print("removing version")
				sceene_container_stage_sublayers.remove(path)
				
				print("adding version") 
				print(os.path.relpath(Sceene_path))
				sceene_container_stage_sublayers.append("./"+os.path.relpath(Sceene_path))
				sceene_container_stage.Save()
			else:
				print("no version off thsi sceene exists will add sceene now ")
				print(os.path.relpath(Sceene_path))
				sceene_container_stage_sublayers.append("./"+os.path.relpath(Sceene_path))
				sceene_container_stage.Save()
				
print("all sublayers")
print(sceene_container_stage_sublayers)
print()
