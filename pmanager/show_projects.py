from os import listdir
from pmanager.res import *

def show_projects(namespace):

    if not path.exists("config/default_path.conf"):

        dirpath = get_home_dir_path()+"/projects"

    else:

        with open("config/default_path.conf","r",encoding="utf-8") as f:

            dirpath = f.read()

    pwarn("listing folders in your default projects directory :")
    
    for folder in listdir(dirpath):
        pinfo(folder)