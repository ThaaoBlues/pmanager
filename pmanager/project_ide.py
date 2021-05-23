from os import path
from xml.etree import ElementTree as ET
from pmanager.res import  pinfo, psuccess



def initialize(namespace):
    project_name = namespace.project_name[0]
    

    command = input("IDE/startup command (manual, so it needs the full path of your project etc...)\n--> ")
    
    #escape some characters

    command.replace("&","&amp;")
    command.replace("\"","&quot;")
    command.replace("'","&apos;")
    command.replace("<","&lt;")
    command.replace(">","&gt;")


    with open(f"config/{project_name}.xml","w") as f:
        f.write(f'<config>\n<ide>{command}</ide>\n</config>')
        f.close()

    psuccess(f"default project IDE/start command is now :\n{command}")




#used in open module to get custom start command
def get_default_ide(project_name):

    root = ET.parse(f"config/{project_name}.xml",).getroot()

    command = root.find("ide").text.replace("\n","")

    pinfo(f"executing : \n{command}")

    return command
