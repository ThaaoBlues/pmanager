from platform import system
from subprocess import run
from os import path
from pmanager.res import *

def initialize(namespace):

    project_name = namespace.project_name[0]

    if not path.exists("config/default_path.conf"):

        dirpath = get_home_dir_path()+"/projects/"+project_name + "/"

    else:

        with open("config/default_path.conf","r",encoding="utf-8") as f:

            dirpath = f.read()+"/"+ project_name +"/"

    pinfo(f"opening project folder : \n {dirpath}")


    if system() == "Linux":
        run(["x-terminal-emulator",f"-e cd {dirpath}"],shell=True)

    elif system() == "Windows":
        run(["start", "cmd.exe", f"@cmd /k cd {dirpath}"],shell=True)