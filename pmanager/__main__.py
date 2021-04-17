
import sys
from pmanager.modules import *
from os import listdir, getcwd
from importlib import import_module
from os import path,mkdir
from functools import partial
import argparse
from subprocess import run
import atexit
from multiprocessing import freeze_support

#importing processing modules
from pmanager.open_project import open_project
import pmanager.delete as delete
import pmanager.share as share
import pmanager.show_projects as show_projects
import pmanager.archive as archive
import pmanager.terminal as terminal
import pmanager.res as res
import pmanager.help_func as help_func
import pmanager.config as config
import pmanager.import_custom as import_custom


def create_new_project(namespace):

    project_name = namespace.project_name[0]
    selected_modules = namespace.modules

    if not path.exists("config/default_path.conf"):
        dirpath = res.get_home_dir_path()+"/projects/"+project_name
    else:
        with open("config/default_path.conf","r") as f:
            dirpath = f.read()+"/"+ project_name


    if path.exists(dirpath):
        res.perror(f"This project already exist : \n {dirpath}")
        return

    modules_list = list(set([path.splitext(x)[0] for x in listdir("pmanager/modules/")]))
    i=1
    for module in selected_modules:
        if module in modules_list:
            try:
                res.pinfo("initializing " + module)
                imported_module = import_module(f"pmanager.modules.{module}")
                imported_module.initialize(project_name)
            except:
                res.perror("Error while initializing " + module)
                print(e)
            i+=1

    open_project(namespace)


def share_code(namespace):

    project_name = namespace.project_name[0]

    if not path.exists("config/default_path.conf"):
        dirpath = res.get_home_dir_path()+"/projects/"+project_name
    else:
        with open("config/default_path.conf","r",encoding="utf-8") as f:
            dirpath = f.read()+"/"+ project_name
    res.write_temp_file("dirpath",dirpath)
    res.write_temp_file("project_name",project_name)
    share.initialize()



def process_args():

    if not path.exists("config"):
        config.initialize()

    if len(sys.argv) <= 1:
        help_func.display_help_message()

    if not path.exists(res.get_home_dir_path()+"/projects"):
        mkdir(res.get_home_dir_path()+"/projects")


    #init parser
    parser = argparse.ArgumentParser(prog='pmanager')
    subparsers = parser.add_subparsers(help="COMMANDS")

    #pmanager projects
    projects_parser = subparsers.add_parser("projects", help="List all projects")
    projects_parser.set_defaults(func=show_projects.show_projects)

    #pmanager new 
    new_project_parser = subparsers.add_parser("new", help="Add a new project")
    new_project_parser.add_argument("project_name", help="Project name", nargs=1)
    new_project_parser.add_argument("modules", help="Modules to import in the project", nargs=argparse.REMAINDER)
    new_project_parser.set_defaults(func=create_new_project)

    #pmanager modlist
    modlist_parser = subparsers.add_parser("modlist", help="List all available projects creation modules")
    modlist_parser.set_defaults(func=help_func.print_modules_list)


    #pmanager help (because the auto help message is ugly)
    help_parser = subparsers.add_parser("help", help="Display help message")
    help_parser.set_defaults(func=help_func.display_help_message)

    #pmanager config
    config_parser = subparsers.add_parser("config", help="Open the configuration menu")
    config_parser.set_defaults(func=config.config_menu)


    #pmanager delete
    delete_parser = subparsers.add_parser("delete", help="delete the specified modules from a project")
    delete_parser.add_argument("project_name", help="Project name", nargs=1)
    delete_parser.add_argument("modules", help="Modules to import in the project", nargs=argparse.REMAINDER)

    delete_parser.set_defaults(func=delete.initialize)

    #pmanager add




    #pmanager open
    open_parser = subparsers.add_parser("open", help="Open the specified project")
    open_parser.add_argument("project_name", help="Project name", nargs=1)
    open_parser.set_defaults(func=open_project)


    #pmanager share
    share_parser = subparsers.add_parser("share", help="Share the code of the specified project")
    share_parser.add_argument("project_name", help="Project name", nargs=1)
    share_parser.set_defaults(func=share_code)
    

    #pmanager archive
    archive_parser = subparsers.add_parser("archive", help="Archive the specified project")
    archive_parser.add_argument("project_name", help="Project name", nargs=1)
    archive_parser.set_defaults(func=archive.initialize)


    #pmanager terminal
    terminal_parser = subparsers.add_parser("terminal", help="Open a terminal on the specified project")
    terminal_parser.add_argument("project_name", help="Project name", nargs=1)
    terminal_parser.set_defaults(func=terminal.initialize)


    #pmanager import
    import_parser = subparsers.add_parser("import", help="Import a custom projects creation module")
    import_parser.set_defaults(func=import_custom.import_custom_module)

    #execute parser
    args = parser.parse_args(sys.argv[1:])
    args.func(args)


    

def main():
    res.auto_chdir_to_file_root()
    atexit.register(res.clear_temp_files)
    process_args()



if __name__ == "__main__":
    freeze_support()
    main()
    

    





