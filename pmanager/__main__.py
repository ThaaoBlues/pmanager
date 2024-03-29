
import sys

from pmanager.modules import *
from os import listdir, getcwd
from importlib import import_module
from os import path,mkdir
import argparse
import atexit
from requests import get
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
import pmanager.project_ide as project_ide
import pmanager.run as run_project
import pmanager.add_run as add_run
import pmanager.edit_project_conf as edit_conf
import pmanager.add as add_module_to_project
import pmanager.clone as clone_from_remote
import pmanager.changelog as changelog
import pmanager.rename as rename_project
import pmanager.edit_module as edit_module
import pmanager.github as github
import pmanager.zip as zip 


from pmanager import __version__


CWD = getcwd()

def create_new_project(namespace):

    project_name = namespace.project_name
    selected_modules = namespace.modules

    if not path.exists("config/default_path.conf"):
        dirpath = res.get_home_dir_path()+"/projects/"+project_name
    else:
        with open("config/default_path.conf","r",encoding ="utf-8") as f:
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
            except Exception as e:
                res.perror("Error while initializing " + module)
                res.pwarn("error message :")
                print(e)
            
            i+=1
    
    # no modules selected, create an empty project
    if selected_modules == []:
        if not path.exists("config/default_path.conf"):
            dirpath = res.get_home_dir_path()+"/projects/"+project_name
        else:
            with open("config/default_path.conf","r",encoding="utf-8") as f:
                dirpath = f.read()+"/"+ project_name

        if not path.exists(dirpath):
                mkdir(dirpath)
                
                
                

    open_project(namespace)



def display_version(namespace):

    l_version = "error while trying to get lastest version on https://pypi.org/pypi/projects-manager/json"

    if res.check_internet():
        r = get("https://pypi.org/pypi/projects-manager/json")
        if r.status_code == 200:
            l_version = str(r.json()['info']['version'])
    
    res.psuccess("current version : "+ __version__ +"\nlastest version : "+l_version+"\n(checked on https://pypi.org/pypi/projects-manager/json)")



def process_args():

    res.notify_update()

    if not path.exists("config"):
        config.initialize()

    if not path.exists(res.get_home_dir_path()+"/projects"):
        mkdir(res.get_home_dir_path()+"/projects")


    #init parser
    parser = argparse.ArgumentParser(prog='pmanager')
    subparsers = parser.add_subparsers(help="COMMANDS")

    #pmanager projects
    args_parser = subparsers.add_parser("version", help="display installed version versus lastest version published on pip")
    args_parser.set_defaults(func=display_version)

    #pmanager projects
    args_parser = subparsers.add_parser("projects", help="List all projects")
    args_parser.set_defaults(func=show_projects.show_projects)

    #pmanager new 
    args_parser = subparsers.add_parser("new", help="Add a new project")
    args_parser.add_argument("project_name", help="project name", nargs="?",default=path.basename(CWD))

    args_parser.add_argument("modules", help="Modules to import in the project", nargs=argparse.REMAINDER)
    args_parser.set_defaults(func=create_new_project)

    #pmanager modlist
    args_parser = subparsers.add_parser("modlist", help="List all available projects creation modules")
    args_parser.set_defaults(func=help_func.print_modules_list)

    #pmanager config
    args_parser = subparsers.add_parser("config", help="Open the configuration menu")
    args_parser.set_defaults(func=config.config_menu)


    #pmanager delete
    args_parser = subparsers.add_parser("delete", help="delete the specified modules from a project")
    args_parser.add_argument("project_name", help="project name", nargs="?",default=path.basename(CWD))

    args_parser.add_argument("modules", help="Modules to import in the project", nargs=argparse.REMAINDER)

    args_parser.set_defaults(func=delete.initialize)

    #pmanager add
    args_parser = subparsers.add_parser("add", help="Add module to an existing project")
    args_parser.add_argument("project_name", help="project name", nargs="?",default=path.basename(CWD))

    args_parser.add_argument("modules", help="Modules to import in the project", nargs=argparse.REMAINDER)
    args_parser.set_defaults(func=add_module_to_project.initialize)



    #pmanager open
    args_parser = subparsers.add_parser("open", help="Open the specified project")
    args_parser.add_argument("project_name", help="project name", nargs="?",default=path.basename(CWD))

    args_parser.set_defaults(func=open_project)


    #pmanager share
    args_parser = subparsers.add_parser("share", help="Share the code of the specified project over your network. Read only.")
    args_parser.add_argument("project_name", help="project name", nargs="?",default=path.basename(CWD))

    args_parser.set_defaults(func=share.initialize)
    

    #pmanager archive
    args_parser = subparsers.add_parser("archive", help="Archive the specified project")
    args_parser.add_argument("project_name", help="project name", nargs="?",default=path.basename(CWD))

    args_parser.set_defaults(func=archive.initialize)


    #pmanager term <project_name>
    args_parser = subparsers.add_parser("term", help="Open a terminal on the specified project's directory")
    args_parser.add_argument("project_name", help="project name", nargs="?",default=path.basename(CWD))

    args_parser.set_defaults(func=terminal.initialize)


    #pmanager import
    args_parser = subparsers.add_parser("import", help="Import a custom project's creation module")
    args_parser.set_defaults(func=import_custom.import_custom_module)


    #pmanager rename
    args_parser = subparsers.add_parser("rename", help="rename a project")
    args_parser.add_argument("old_project_name", help="old project name", nargs=1)
    args_parser.add_argument("new_project_name", help="new project name", nargs=1)
    args_parser.set_defaults(func=rename_project.initialize)


    #pmanager changelog
    args_parser = subparsers.add_parser("changelog", help="read the changelog")
    args_parser.set_defaults(func=changelog.initialize)


    #pmanager clone
    args_parser = subparsers.add_parser("clone", help="clone a remote git repository and create a project with.")
    args_parser.add_argument("git_url", help="git remote repository url", nargs=1)
    args_parser.add_argument("project_name", help="future project name", nargs=1)
    args_parser.set_defaults(func=clone_from_remote.initialize)

    #pmanager ide <project_name>
    args_parser = subparsers.add_parser("ide", help="Change the default ide only to the specified project")
    args_parser.add_argument("project_name", help="project name", nargs="?",default=path.basename(CWD))

    args_parser.set_defaults(func=project_ide.initialize)


    #pmanager add_run <project name> <command>
    args_parser = subparsers.add_parser("add_run", help="add a run command that will\
be executed when you use \"pmanager < project name > run\"\
(you can add as many commands as you want !)")

    args_parser.add_argument("project_name", help="project name", nargs="?",default=path.basename(CWD))

    args_parser.add_argument("command", help="Command to add to the project run", nargs=1)
    args_parser.set_defaults(func=add_run.initialize)


    #pmanager edit_conf <project name>
    args_parser = subparsers.add_parser("edit_conf", help="open the configurations xml file for\
a specified project in your default code editor,\
so you can directly edit run and startup commands.")

    args_parser.add_argument("project_name", help="project name", nargs="?",default=path.basename(CWD))

    args_parser.set_defaults(func=edit_conf.initialize)
    

    #pmanager run <project name>
    args_parser = subparsers.add_parser("run", help="run all the commands you have specified with\
the command above (chronological order)\n")

    args_parser.add_argument("project_name", help="project name", nargs="?",default=path.basename(CWD))

    args_parser.set_defaults(func=run_project.initialize)


    #pmanager edit_module <module_name>
    args_parser = subparsers.add_parser("edit_module", help="open the source files of an existing module so you can personalize it")
    args_parser.add_argument("module_name", help="Module to edit", nargs=1)
    args_parser.set_defaults(func=edit_module.initialize)


    #pmg add_github <project_name>
    args_parser = subparsers.add_parser("add_github", help="link a project to its github")
    args_parser.add_argument("owner_slash_repository_name", help="github <owner>/<repository_name>", nargs=1)
    args_parser.add_argument("project_name", help="project name", nargs="?",default=path.basename(CWD))

    args_parser.set_defaults(func=github.add_project)
    
    
    #pmg issues <project_name>
    args_parser = subparsers.add_parser("issues", help="view issues of a project if linked to a github repo")
    args_parser.add_argument("project_name", help="project name", nargs="?",default=path.basename(CWD))

    args_parser.set_defaults(func=github.get_project_issues)
    
    #pmg zip <project_name>
    args_parser = subparsers.add_parser("zip", help="Compress a project into a zip file.")
    args_parser.add_argument("project_name", help="project name", nargs="?",default=path.basename(CWD))
    args_parser.set_defaults(func=zip.initialize)



    #if nothing is passed, add the help option
    if len(sys.argv) == 1:
        sys.argv.append("-h")
    
    
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
    

    





