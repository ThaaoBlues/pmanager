from subprocess import run
from os import path, getcwd
from pmanager.res import *
from pmanager.project_ide import get_default_ide

def open_project(namespace):

    project_name = namespace.project_name[0]

    
    if not path.exists("config/default_path.conf"):

        dirpath = get_home_dir_path()+"/projects/"+project_name + "/"

    else:

        with open("config/default_path.conf","r",encoding="utf-8") as f:

            dirpath = f.read()+"/"+ project_name +"/"

    pinfo(f"opening project folder : \n {dirpath}")

    #check if the project exists
    if not path.exists(dirpath):
        perror("This project doest not exists")

    else:
        #check if a custom start command is specified for the project
        if path.exists(f"config/{project_name}.xml"):
            run(get_default_ide(project_name),shell=True)

        #if not, run the usual default command
        else:
            with open("config/default_ide.conf","r") as f:

                run([f.read(),""+dirpath+"."],shell=True)


def open_project_str(project_name):
 
    if not path.exists("config/default_path.conf"):

        dirpath = get_home_dir_path()+"/projects/"+project_name + "/"

    else:

        with open("config/default_path.conf","r",encoding="utf-8") as f:

            dirpath = f.read()+"/"+ project_name +"/"

    pinfo(f"opening project folder : \n {dirpath}")

    #check if the project exists
    if not path.exists(dirpath):
        perror("This project doest not exists")

    else:
        #check if a custom start command is specified for the project
        if path.exists(f"config/{project_name}.xml"):
            run(get_default_ide(project_name),shell=True)

        #if not, run the usual default command
        else:
            with open("config/default_ide.conf","r") as f:

                run([f.read(),""+dirpath+"."],shell=True)