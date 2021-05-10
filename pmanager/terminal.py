from platform import system
from subprocess import run, check_call, CalledProcessError
from re import split as sep
from os import path, getenv
from pmanager.res import *
from distro import id
from multiprocessing import Process

def run_cmd(cmd):
    """
    :raise: CalledProcessError

    """
    try:
        check_call(cmd,shell=True,close_fds=True)
    except CalledProcessError:
        raise CalledProcessError



def initialize(namespace):

    ARCH_DISTRO = ["garuda","arch","blackarch","manjaro"]
    DEBIAN_DISTRO = ["ubuntu","debian","mint","kali","parrot"]

    project_name = namespace.project_name[0]

    if not path.exists("config/default_path.conf"):

        dirpath = get_home_dir_path()+"/projects/"+project_name + "/"

    else:

        with open("config/default_path.conf","r",encoding="utf-8") as f:

            dirpath = f.read()+"/"+ project_name +"/"

    pinfo(f"opening project folder : \n {dirpath}")
    
    


    if system() == "Linux":
        
        term_emulator = sep("-| ",getenv('TERM'))[0].strip("\n")

        pinfo(f"detected default terminal emulator : {term_emulator}")

        try:
            Process(target=run_cmd,args=(f"{term_emulator} --workdir {dirpath}",)).start()

            pwarn(f"running : {term_emulator} --workdir {dirpath}")
        except CalledProcessError:
            try:
                Process(target=run_cmd,args=(f"{term_emulator} --working-directory {dirpath}",)).start()

                pwarn(f"running : {term_emulator} --working-directory {dirpath}")
            except CalledProcessError:
                try:
                    Process(target=run_cmd,args=(f"{term_emulator} --w {dirpath}",)).start()

                    pwarn(f"running : {term_emulator} --w {dirpath}")
                except CalledProcessError:
                    perror("Sorry, pmanager is not yet able to identify and start an instance of your terminal")

    
    
    elif system() == "Windows":
        run(["start", "cmd.exe", f"@cmd /k cd {dirpath}"],shell=True)