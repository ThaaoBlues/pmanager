from socket import gethostname, gethostbyname_ex,create_connection
from requests import get
from datetime import datetime
from random import randint
from os import listdir, remove,chdir,path,getcwd
from platform import system, platform, python_version
from colorama import Fore, Back, Style
from colorama import init
from pathlib import Path
import pmanager



def notify_update():
    """
    request the lastest version number of the project to pypi
    and notify the user if his version is outdated

    """

    res = get("https://pypi.org/pypi/projects-manager/json").json()
    if str(pmanager.__version__) != str(res['info']['version']):
        pwarn("A new version of pmanager is available, to update it just type 'pip install --upgrade projects_manager'")





def check_internet():
    """
    a simple function to check if an internet connection is available
    :return: True if connected, else it returns false
    """
    try:
        create_connection(("1.1.1.1", 53),2)
        return True
    except:
        return False



def is_available(website, port = None):
    """
    a simple function to check if a website/server is available
    :param: website is a string where you put the website url/ip
    :param: port is an optionnal argument where you can specify a port
    :return: True if available, else it returns false
    """
    if port !=None:
        try:
            create_connection((website, port),2)
            return True
        except:
            return False
    else:
        try:
            create_connection((website, 80),2)
            return True
        except:
            return False



def get_os_name():
    """
    :return: the os name
    """
    return str(system())



def get_full_os_name():
    """
    :return: the full os name
    """
    return str(platform())



def get_python_version():
    """
    :return: the python version you are using
    """
    return str(python_version())



def get_file_number_of_lines(fname):
    """
    :param: fname is a string containing the path to the file you want to count the lines
    :return: the number of line of the file
    """
    with open(f"{getcwd()}/{fname}") as f:
        for i, l in enumerate(f):
            pass
    return i + 1



def get_file_size(fname):
    """
    :param: fname is a string containing the path to the file you want to get the size
    :return: a string containing the size of the file in Megabytes
    """
    byte = int(path.getsize(f"{getcwd()}/{fname}"))
    return f"{byte/1000000}"




def perror(str,time=False):
    """
    :param: time is set to false by default, set to true it display the time with the message
    :param: str is just a string where you put your message
    This function display a error-style custom and colored error message
    """
    init()
    if time:
        print(f"{Fore.RED}{gettime()} [x] {str} {Fore.WHITE}")
    else:
        print(f"{Fore.RED}[x] {str} {Fore.WHITE}")



def pwarn(str,time=False):
    """
    :param: time is set to false by default, set to true it display the time with the message
    :param: str is just a string where you put your message
    This function display a warning-style custom and colored warning message
    """
    init()
    if time:
        print(f"{Fore.YELLOW}{gettime()} [!] {str} {Fore.WHITE}")
    else:
        print(f"{Fore.YELLOW}[!] {str} {Fore.WHITE}")




def pinfo(str,time=False):
    """
    :param: time is set to false by default, set to true it display the time with the message
    :param: str is just a string where you put your message
    This function display a info-style custom and colored info message
    """
    init()
    if time:
        print(f"{Fore.BLUE}{gettime()} [+] {str} {Fore.WHITE}")
    else:
        print(f"{Fore.BLUE}[+] {str} {Fore.WHITE}")




def psuccess(str,time=False):
    """
    :param: time is set to false by default, set to true it display the time with the message
    :param: str is just a string where you put your message
    This function display a success-style custom and colored success message
    """
    init()
    if time:
        print(f"{Fore.GREEN}{gettime()} [v] {str} {Fore.WHITE}")
    else:
        print(f"{Fore.GREEN}[v] {str} {Fore.WHITE}")




def get_private_ips():
    """
    :return: a list of all private IP addresses liked to your machine (may be vm) 
    """
    return gethostbyname_ex(gethostname())[:2]



def get_public_ip():
    """
    :return: a string containing your public ip
    """
    return get('https://api.ipify.org').text




def get_hostname():
    """
    :return: a string containing the hostname
    """
    return gethostname()




def get_time():
    """
    :return: a string containing the time
    """
    now = datetime.now()
    return now.strftime("%H:%M:%S")





def get_date():
    """
    :return: a string containing today's date
    """
    today = datetime.today()
    return today.strftime("%d/%m/%Y")




def write_temp_file(purpose,content,append=True):
    """
    :param: purpose is a string where you specify an idea of what you are putting in the temp file
    :param: content is a string where you put the content of the temp file
    :param: append is a boolean set to True by default to open the temp file in append mode or not
    write the specified string on a random named temp file
    """
    if append: mode = "a" 
    else: mode = "w"
    with open(str(randint(0,99999999999))+purpose+".res",mode) as f:
        f.write(content)
        f.close()



def read_temp_file(purpose):
    """
    :param: purpose is a string  where ypu specify an idea of what you have put in the temp file
    :return: a string containing the content of the temp file or False if the file for this purpose don't exist
    """
    found = False
    for file in listdir():
        if (purpose in file) and (".res" in file):
            found = True
            with open(file) as f:
                content = f.read()
                f.close()
    
    if not found:
        return False
    else:
        return content
            

def clear_temp_files():
    """
    delete all temporary files created by write_temp_file
    """
    for file in listdir():
        if (".res" in file):
            remove(file)



def auto_chdir_to_file_root():
    """
    a function to make sure that the program is writing/reading at his root 
    (need to put res file in a folder)
    """
    chdir(path.abspath(__file__).replace("res.py",""))
    chdir("..")



def get_home_dir_path():
    """
    :return: a string containing the path to the home directory of the curent user
    """

    return str(Path.home())
