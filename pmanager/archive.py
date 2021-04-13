from os import path
from shutil import move
from pmanager.res import *


def initialize(namespace):
    
    project_name = namespace.project_name[0]

    if not path.exists("config/default_path.conf"):

        dirpath = get_home_dir_path()+"/projects/"+project_name + "/"

    else:

        with open("config/default_path.conf","r",encoding="utf-8") as f:

            dirpath = f.read()+"/"+ project_name +"/"
    

    if not path.exists("config/default_archive_path.conf"):

        archive_dirpath = get_home_dir_path()+"/projects_archive/"+project_name + "/"

    else:

        with open("config/default_archive_path.conf","r",encoding="utf-8") as f:

            archive_dirpath = f.read()+"/"+ project_name +"/"


    pinfo(f"opening project folder : \n {dirpath}")

    pinfo(f"moving it to : \n {archive_dirpath}")

    move(dirpath,archive_dirpath)

    psuccess("project archived !")