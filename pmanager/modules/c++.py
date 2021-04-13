from pmanager.res import *
from os import mkdir,path


def initialize(project_name):
    if not path.exists("config/default_path.conf"):
        dirpath = get_home_dir_path()+"/projects/"+project_name
    else:
        with open("config/default_path.conf","r",encoding="utf-8") as f:
            dirpath = f.read()+"/"+ project_name

    if not path.exists(dirpath):
            mkdir(dirpath)
        
    module_name = path.basename(__file__).replace(".py","")

    with open(f"pmanager/modules/{module_name}.act","r") as f:
        lines = f.read().split('\n')
        f.close()

    folders = []
    for line in lines:


        if (line.startswith("   ") and "." in line):
           
            create_file(folders[-1],line.strip("    "),module_name,dirpath)

        else :
            line = line.replace("   ","")
            folders.append(line)
            if not path.exists(f"{dirpath}/{line}"):
                mkdir(f"{dirpath}/{line}")



def create_file(folder,filename,module_name,dirpath):

    with open(f"pmanager/modules/{module_name}.template","r") as f:
        lines = f.read().split('\n')
        
        for i in range(len(lines)):

            if lines[i] in filename:
                with open(f"{dirpath}/{folder}/{filename}","w") as f2:
                    
                    j = 0
                    rest = lines[lines.index(f"Filename : {filename}")+2:]
                    while not "End template" in rest[j]:

                        f2.write(rest[j]+"\n")

                        j += 1
           
