# projects_manager

[![Downloads](https://static.pepy.tech/personalized-badge/projects-manager?period=total&units=none&left_color=black&right_color=blue&left_text=Downloads%20with%20pip)](https://pypi.org/project/projects-manager/)


A simple projects manager/creator I use for myself and grow little by little, it may not work sometimes.
type "python -m pmanager -h" to get a simple introduction

the default ide used by the script is VScode, use "python pmanager.py config" to change it.

example :
if you are using visual studio code, open the  configuration menu, select change default ide and type "code" in the prompt. 
(because the shell command to open vscode is : "code [yourfolder]" )

The project manager is based on personnalisable modules, they are all in the modules folder and called when you specify them at the creation/add module action of a project.

## Use :


- **pmanager new < project name > [module]**
    
    Create a new project with de desired module configuration



- **pmanager < project name > add [module]**
    
    
    Add a module to an existing project



- **pmanager delete < project_name > all/[module]**
    
    
    Delete all project or only a list of modules



- **pmanager share < project name >**
    
    
    Open a tiny webserver to share your project source code over
    the network



- **pmanager config**


    Start pmanager configuration script



- **pmanager add < project name > [module]**
    
    
    add a module/list of modules to an existing project


- **pmanager open < project name >**


    open a project


- **pmanager modlist**


    get a list of all available modules


- **pmanager projects**


    get a list of all projects


- **pmanager archive < project name >**


    archive a specific project 
    (default archives folder is <user home directory>/projects_archive)


- **pmanager terminal < project name >**


    open your default terminal at the specified project folder

- **pmanager import**

    start the assistant to create a custom project creation module

- **pmanager ide < project name >**

    
    start the assistant to replace the default ide command by your custom manual startup command for the specified project

- **pmanager add_run < project name > < command >**


    add a run command that will be executed when you use "pmanager < project name > run"
    (you can add as many commands as you want !)

- **pmanager run < project name >**
    

    run all the commands you have specified with the command above (chronological order)


- **pmanager edit_conf < project name >**

    open the configurations xml file for a specified project in your default code editor, so you can directly edit run and startup commands.


- **pmanager version**

    display installed version versus lastest version published on pip


- **pmanager clone < git_remote_url > < project_name >**

    clone a remote git repository and create a project with.


- **pmanager remame < old_name > < new_name >**

    rename a project

- **pmanager changelog**

    read the changelog


- **pmanager edit_module < module_name >**

    open the source files of an existing module so you can personalize it


- **example :**

  
- pmanager new my_project python flask
  

- pmanager open my_project
  

- pmanager delete my_project all
  

- pmanager terminal my_project

  
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
