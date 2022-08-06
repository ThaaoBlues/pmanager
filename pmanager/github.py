from requests import get
from pmanager.res import *
from xml.etree import ElementTree as ET


def add_project(namespace):
    
    project_name = namespace.project_name
    
    github = namespace.owner_slash_repository_name[0]
    
    
    if not path.exists("config/default_path.conf"):
        dirpath = get_home_dir_path()+"/projects/"+project_name
    else:
        with open("config/default_path.conf","r",encoding="utf-8") as f:
            dirpath = f.read()+"/"+ project_name

    if not path.exists(dirpath):
        perror(f"This project does not exist : \n {dirpath}")
        
        exit(1)
    
    
    if not "/" in github:
        perror("Your github username and repo must follow this pattern : <owner>/<repository_name>")
        exit(1)
        
        
    github = github.split("/")
    github = {"owner":github[0],"repo":github[1]}
    
    config_file = f"config/{project_name}.xml"
    
    if not path.exists(config_file):
        with open(config_file,"w") as f:
            f.write("<config></config>")
            f.close()
        
        
    tree = ET.parse(config_file,)
    
    root = tree.getroot()
    
    ele = ET.Element("github")
    
    ele.attrib["owner"] = github["owner"]
    ele.attrib["repo"] = github["repo"]
    
    root.append(ele)
    
    tree.write(config_file)
    
    psuccess(f"added the github repo of {project_name}, you may now see the issues by using \"pmg issues {project_name}\"")

    
        
        
        
def get_project_issues(namespace):
    
    
    project_name = namespace.project_name[0]    
    
    if not path.exists("config/default_path.conf"):
        dirpath = get_home_dir_path()+"/projects/"+project_name
    else:
        with open("config/default_path.conf","r",encoding="utf-8") as f:
            dirpath = f.read()+"/"+ project_name

    if not path.exists(dirpath):
        perror(f"This project does not exist : \n {dirpath}")
        
        exit(1)
        
        
        
    config_file = f"config/{project_name}.xml"
    
    if not path.exists(config_file):
        perror("no github repository have been linked to this project, use \"pmg add_github <project_name> <owner>/<repo>\" to add one.")
        exit(1)
        
    
    
    root = ET.parse(config_file).getroot()
    
    found = False
    for item in root:
        
        if item.tag == "github":
            
            url = f"https://api.github.com/repos/{item.attrib['owner']}/{item.attrib['repo']}/issues"
            
            found = True
            
    if not found:
    
        perror("no github repository have been linked to this project, use \"pmg add_github <project_name> <owner>/<repo>\" to add one.")
        exit(1)    


    try:
        json_res = get(url).json()

        for ele in json_res:
            
            if ele["state"] == "open":
                pwarn(ele["title"])
                psuccess("|---"+ele["html_url"])
        
    except Exception as e:
        perror("an error occured while requesting github api. No internet or wrong repo name ?")
        pinfo(e)
        exit(1)