from os import path,mkdir,remove
from pmanager.res import *

def initialize(namespace):

    project_name = namespace.project_name[0]
    modules_name = namespace.modules

    if not path.exists("config/default_path.conf"):
        dirpath = get_home_dir_path()+"/projects/"+project_name
    else:
        with open("config/default_path.conf","r",encoding="utf-8") as f:
            dirpath = f.read()+"/"+ project_name

    pinfo(f"removing folder : \n {dirpath}")
    if not path.exists(dirpath):
        perror(f"This project does not exist : \n {dirpath}")

    else:
        for module in modules_name:
            try:
                if module == "all":
                    remove(dirpath)
                    #remove the custom startup command if there is one
                    if path.exists("config/{project_name}.xml"):
                        remove(f"config/{project_name}.xml")

                    break
                else:
                    remove(dirpath+"/"+module+"_files")
            except :
                perror("An error occured while removing your files (it may be just that you are not administrator)")
                exit(1)

        psuccess("Successfully removed your files")
