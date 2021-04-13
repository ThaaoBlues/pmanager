from pmanager.res import*
from os import path
from shutil import copyfile

def import_custom_module(namespace):

    pwarn("To know how to design your custom projects module, please refer you to : \nhttps://www.github.com/ThaaoBlues/pmanager/blob/main/README.MD")

    module_name = input("module name : \n-->")
    module_script_path = input("module script path (.py) \n-->")
    module_files_act_path = input("module files architecture file path (.act) \n-->")
    module_files_content_path = input("modules files content file path (.template) \n-->")

    pinfo("copying files")

    if path.exists(f"pmanager/modules/{module_name}.py"):
        perror("this projects module already exists")
    else:
        copyfile(module_script_path,f"pmanager/modules/{module_name}.py")
        copyfile(module_files_act_path,f"pmanager/modules/{module_name}.act")
        copyfile(module_files_content_path,f"pmanager/modules/{module_name}.template")

        psuccess(f"new module {module_name} added !")