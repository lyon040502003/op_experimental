import os 
from pxr import Usd

Sceenes_Foulder = hou.parm("Sceene_Foulder").evalAsString()
Sceene_Name = hou.parm("Sceene_name").evalAsString()

version = hou.parm("version").eval()
inc = hou.parm("inc").eval()

sceene_foulder = os.path.join(Sceenes_Foulder, (Sceene_Name + "_SCEENE"))
msci_path = os.path.join(sceene_foulder, "msci")

sceene_container_path = os.path.join(sceene_foulder, (Sceene_Name + "_SCEENE_CONTAINER.usda"))






# create sceene foulder
try:
	os.mkdir(sceene_foulder)
	os.mkdir(msci_path)

except:
	print("foulder_allredy_exists")


# create sceene container 
all_fils_in_sceene_path = os.listdir(sceene_foulder)
os.chdir(sceene_foulder)
if not sceene_container_path in [os.path.abspath(files) for files in all_fils_in_sceene_path]:
	print("no container found")
	Usd.Stage.CreateNew(sceene_container_path)
	print("created container")
else:
	print("container allredy exists")
	
	
# check if sceene versoin exists 

version_number_padded = f'{version:02}'
inc_number_padded = f'{inc:03}'

selected_sceene_version = os.path.join(sceene_foulder, (Sceene_Name + "_SCEENE_v" + version_number_padded + "_" + inc_number_padded + ".usd"))


if selected_sceene_version in [os.path.abspath(files) for files in all_fils_in_sceene_path]:
	print("the version off the sceene allredy exists if you want to create a new version this is the wrong tool")
else:
	print("there is no sceene with this version will create now ")
	Usd.Stage.CreateNew(selected_sceene_version)
	print(selected_sceene_version)


#Usd.Stage.CreateNew(









