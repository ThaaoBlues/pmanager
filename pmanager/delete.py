from os import path,mkdir,remove
from pmanager.res import *

def initialize(namespace):

    print(namespace)
    project_name = namespace.project_name[0]
    modules_name = namespace.modules

    if not path.exists("config/default_path.conf"):
        dirpath = get_home_dir_path()+"/projects/"+project_name
    else:
        with open("config/default_path.conf","r") as f:
            dirpath = f.read()+"/"+ project_name

    if not path.exists(dirpath):
        perror(f"This project does not exist : \n {dirpath}")

    else:
        for module in modules_name:
            try:
                if module == "all":
                    remove(dirpath)
                    break
                else:
                    remove(dirpath+"/"+module+"_files")
            except :
                perror("An error occured while removing your files (it may be just that you are not administrator)")
        
        psuccess("Successfully removed your files")
