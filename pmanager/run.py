from os import path
from subprocess import run
from xml.etree import ElementTree as ET
from pmanager.res import perror, pinfo, psuccess

def get_run_commands(project_name):
    """
    parsing the xml and return run commands

    """
    root = ET.parse(f"config/{project_name}.xml",).getroot()

    command = [ i.text.replace("\n","") for i in root.findall("run")]

    return command




def initialize(namespace):
    """
    called by argparse

    """

    project_name = namespace.project_name[0]


    #check if a custom start command is specified for the project
    if path.exists(f"config/{project_name}.xml"):

        for command in get_run_commands(project_name):
            pinfo(f"running : {command}")
            out = run(command,shell=True,capture_output=True)
            psuccess(out.stdout.decode("utf-8"))

    else:
        perror("no run command(s) specified for this project,\
            \n run \"python -m pmanager <project name> add_run <command>\" to add a\
            run command\n (you can add as many commands as you want !)")

    