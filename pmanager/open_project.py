from subprocess import run
from os import path, getcwd
from pmanager.res import *


def open_project(namespace):

    project_name = namespace.project_name[0]

    
    if not path.exists("config/default_path.conf"):

        dirpath = get_home_dir_path()+"/projects/"+project_name + "/"

    else:

        with open("config/default_path.conf","r",encoding="utf-8") as f:

            dirpath = f.read()+"/"+ project_name +"/"

    pinfo(f"opening project folder : \n {dirpath}")

    with open("config/default_ide.conf","r") as f:
        
        run([f.read(),""+dirpath+"."],shell=True)
