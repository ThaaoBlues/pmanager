# projects_manager

[![Downloads](https://static.pepy.tech/personalized-badge/projects-manager?period=total&units=none&left_color=black&right_color=blue&left_text=Downloads%20with%20pip)](https://pypi.org/project/projects-manager/)


A simple projects manager/creator I use for myself and grow little by little, it may not work sometimes.
type "python -m pmanager -h" to get a simple introduction

the default ide used by the script is VScode, use "python pmanager.py config" to change it.

example :
if you are using visual studio code, open the  configuration menu, select change default ide and type "code" in the prompt. 
(because the shell command to open vscode is : "code [yourfolder]" )

The project manager is based on personnalisable modules, they are all in the modules folder and called when you specify them at the creation/add module action of a project.

## Usage : ( you can omit the project name if you already are in its directory )


- **pmg new < project name > [module]**
    
    Create a new project with de desired module configuration



- **pmg < project name > add [module]**
    
    
    Add a module to an existing project



- **pmg delete < project_name > all/[module]**
    
    
    Delete all project or only a list of modules



- **pmg share < project name >**
    
    
    Open a tiny webserver to share your project source code over
    the network



- **pmg config**


    Start pmanager configuration script :
        - global default ide
        - global default terminal
        - global default projects path
        - global default projects archiving path
        - reset all settings except projects/archiving path



- **pmg add < project name > [module]**
    
    
    add a module/list of modules to an existing project


- **pmg open < project name >**


    open a project


- **pmg modlist**


    get a list of all available modules


- **pmg projects**


    get a list of all projects


- **pmg archive < project name >**


    archive a specific project 
    (default archives folder is <user home directory>/projects_archive)


- **pmg term < project name >**


    open your default terminal at the specified project folder

- **pmg import**

    start the assistant to create a custom project creation module

- **pmg ide < project name >**

    
    start the assistant to replace the default ide command by your custom manual startup command for the specified project

- **pmg add_run < project name > < command >**


    add a run command that will be executed when you use "pmg < project name > run"
    (you can add as many commands as you want !)

- **pmg run < project name >**
    

    run all the commands you have specified with the command above (chronological order)


- **pmg edit_conf < project name >**

    open the configurations xml file for a specified project in your default code editor, so you can directly edit run and startup commands.


- **pmg version**

    display installed version versus lastest version published on pip


- **pmg clone < git_remote_url > < project_name >**

    clone a remote git repository and create a project with.


- **pmg remame < old_name > < new_name >**

    rename a project

- **pmg changelog**

    read the changelog


- **pmg edit_module < module_name >**

    open the source files of an existing module so you can personalize it


- **pmg add_github < owner >/< repo > < project_name >**

    link a github repository to a project


- **pmg issues < project_name >**

    display all open issues and their html link of a project. Needs to be linked to a github repo with the command just above.

- **pmg zip < project_name >**
    to pack your whole project into a zip archive, available at your project's root as < project_name >.zip

- **example :**

- pmg new my_project python flask
  

- pmg open my_project
  

- pmg delete my_project all
  

- pmg term my_project

  
## additional informations:

- no need to put ``python -m `` before pmanager, a binary is already in the package and put in path


## A module is constitued of two files :

- A python script that contain a initialize()  and recursive() functions that must begin by this code :


```python

from pmanager.res import *
from os import mkdir,path
from xml.etree import ElementTree as ET


def recursive(root,path):
    for item in root:

        if item.tag == "folder":
            sub_path = item.attrib['path']
            print(f"folder : {path}{sub_path}")
            mkdir(f"{path}{sub_path}")
            recursive(item,f"{path}{sub_path}/")

            
        elif item.tag == "file":
            fname = item.attrib['name']
            print(f"file : {path}{fname}")
            with open((path+fname),"w") as f:
                f.write(item.text)
                f.close()


def initialize(project_name):
    if not path.exists("config/default_path.conf"):
        dirpath = get_home_dir_path()+"/projects/"+project_name
    else:
        with open("config/default_path.conf","r",encoding="utf-8") as f:
            dirpath = f.read()+"/"+ project_name

    if not path.exists(dirpath):
            mkdir(dirpath)
        
    module_name = path.basename(__file__).replace(".py","")

    root = ET.parse(f"pmanager/modules/{module_name}.xml",).getroot()

    recursive(root,dirpath+"/")
    


 ```



- And a < modulename >.xml file that has the same name as the module and script and basically store the content of the files and the folder architecture for your module . (template tag can be empty)

It must looks like this (obviously adapt the file name and the template content):


```xml
    
<?xml version="1.0"?>

<template>

    <folder path="c++_files">

        <file name="main.cpp">
#include &lt;iostream&gt;

int main() {
    std::cout &lt;&lt; &quot;Hello World!&quot;
    return 0;
}
        </file>

        <folder path="headers">
            <file name="header_file.hpp">
            
            </file>
        </folder>

    </folder>




</template>

    
```

/!\ Don't forget to escape :

```
" to  &quot;
' to  &apos;
< to  &lt;
> to  &gt;
& to  &amp;
```


___



#### If you like pmanager, don't forget to leave a star on my [github repo](https://www.github.com/thaaoblues/pmanager) ;) 
