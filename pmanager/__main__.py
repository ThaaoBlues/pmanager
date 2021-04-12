
import sys
from pmanager.modules import *
from os import listdir, getcwd
from importlib import import_module
from os import path,mkdir

from subprocess import run
import atexit

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





def process_args():


    if not path.exists("config"):
        config.initialize()

    if not path.exists(res.get_home_dir_path()+"/projects"):
        mkdir(res.get_home_dir_path()+"/projects")

    if len(sys.argv) == 1:
        help_func.display_help_message()

    elif "projects" == sys.argv[1]:
        show_projects.show_projects()

    elif "modlist" == sys.argv[1]:
        help_func.print_modules_list()

    elif "help" == sys.argv[1]:
        help_func.display_help_message()

    elif "config" == sys.argv[1]:
        config.config_menu()

    elif "delete" == sys.argv[1]:
        delete.initialize(sys.argv[3],sys.argv[2])

    elif "add" == sys.argv[1]:
        print("coming soon")

    elif "open" == sys.argv[1]:
        open_project(sys.argv[2])


    elif "share" == sys.argv[1]:

        if not path.exists("config/default_path.conf"):
            dirpath = res.get_home_dir_path()+"/projects/"+sys.argv[2]
        else:
            with open("config/default_path.conf","r",encoding="utf-8") as f:
                dirpath = f.read()+"/"+ sys.argv[2]



        res.write_temp_file("dirpath",dirpath)
        res.write_temp_file("project_name",sys.argv[2])

        share.initialize()


    elif "archive" == sys.argv[1]:
        archive.initialize(sys.argv[2])

    elif "terminal" == sys.argv[1]:
        terminal.initialize(sys.argv[2])
        


    elif "new" == sys.argv[1]:

        modules_list = list(set([path.splitext(x)[0] for x in listdir("modules/")]))
        i=1
        for module in sys.argv[2:]:
            if module in modules_list:
                try:
                    res.pinfo("initializing " + module)
                    imported_module = import_module(f"modules.{module}")
                    imported_module.initialize(sys.argv[2])
                except:
                    res.perror("Error while initializing " + module)
                    print(e)

                i+=1

        open_project(sys.argv[2])



def main():
    res.auto_chdir_to_file_root()
    atexit.register(res.clear_temp_files)
    process_args()



if __name__ == "__main__":
    main()
    

    





