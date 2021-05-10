 projects_manager
A simple projects manager/creator I use for myself and grow little by little, it may not work sometimes.
type "python -m pmanager help" to get a simple introduction

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



- **pmanager delete all/[module] < project_name >**
    
    
    Delete all project or only a module



- **pmanager share < project name >**
    
    
    Open a tiny webserver to share your project source code over
    the network



- **pmanager config**


    Start pmanager configuration script



- **pmanager add [module] < project name >**
    
    
    add a module to an existing project (not available yet)


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


    start the assistant to import a custom project module


- **example :**


python -m pmanager new my_project python flask


python -m pmanager open my_project


python -m pmanager terminal my_project





## A module is constitued of three files :

- A python script that contain a initialization()  and create_file functions that must begin by this code :


```python


from pmanager.res import *
from os import mkdir,path


def initialize(project_name):
    if not path.exists("config/default_path.conf"):
        dirpath = get_home_dir_path()+"/projects/"+project_name
    else:
        with open("config/default_path.conf","r",encoding="utf-8") as f:
            dirpath = f.read()+"/"+ project_name

    if not path.exists(dirpath):
            mkdir(dirpath)
        
    module_name = path.basename(__file__).replace(".py","")

    with open(f"pmanager/modules/{module_name}.act","r") as f:
        lines = f.read().split('\n')
        f.close()

    folders = []
    for line in lines:


        if (line.startswith("   ") and "." in line):
           
            create_file(folders[-1],line.strip("    "),module_name,dirpath)

        else :
            line = line.replace("   ","")
            folders.append(line)
            if not path.exists(f"{dirpath}/{line}"):
                mkdir(f"{dirpath}/{line}")



def create_file(folder,filename,module_name,dirpath):

    with open(f"pmanager/modules/{module_name}.template","r") as f:
        lines = f.read().split('\n')
        
        for i in range(len(lines)):

            if lines[i] in filename:
                with open(f"{dirpath}/{folder}/{filename}","w") as f2:
                    
                    j = 0
                    rest = lines[lines.index(f"Filename : {filename}")+2:]
                    while not "End template" in rest[j]:

                        f2.write(rest[j]+"\n")

                        j += 1
           

           
       
 ```



- A modulename.template file that has the same name as the module and script and basically store the content of the files for your module. (it can be empty)

It must looks like this (obviously adapt the file name and the template content):


```
    
    
Filename : main.py
Begin template
import os
import sys
import pandas as pd
import numpy as np

def hello_world():
    print("hello world !")


End template
Filename : res.py
Begin template
import os
    
End template
    
    
```

- And a modulename.act file tha specify wich folders and files needs to be created and where to place it

It must looks like this :

```

python_files
    main.py
python_files\utils
    res.py


```



