from os import path,mkdir,remove
from pmanager.res import *
def initialize(project_name,modules_name):
    if not path.exists("config/default_path.conf"):
        dirpath = get_home_dir_path()+"/projects/"+project_name
    else:
        with open("config/default_path.conf","r") as f:
            dirpath = f.read()+"/"+ project_name

    if not path.exists(dirpath):
        perror(f"This project does not exist : \n {dirpath}")

    else:
        try:
            if modules_name == "all":
                remove(dirpath)
            else:
                remove(dirpath+"/"+modules_name+"_files")

            psuccess("Successfully removed your files")
        
        except :
            perror("An error occured while removing your files (it may be just that you are not administrator)")
