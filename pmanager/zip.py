from pmanager.res import *
from zipfile import ZIP_DEFLATED, ZipFile
from os import walk

def initialize(namespace):

    project_name = namespace.project_name[0]

    if not path.exists("config/default_path.conf"):
        dirpath = get_home_dir_path()+"/projects/"+project_name
    else:
        with open("config/default_path.conf","r",encoding="utf-8") as f:
            dirpath = f.read()+"/"+ project_name

    if not path.exists(dirpath):
        perror(f"This project does not exist : \n {dirpath}")
        exit(1)
        
        
    # zipping project
    
    pinfo("Compressing project using ZIP_DEFLATED method... (zip file available at your project's root)")
    
        
    
    z = ZipFile(f"{dirpath}/{project_name}.zip","w",ZIP_DEFLATED)
    
    for root,dirs,files in walk(dirpath):
    
        for file in files:
            
            if not file == f"{project_name}.zip": # it would be dumb to pack the archive while writing the archive
                arcname = path.join(root.replace(dirpath,project_name),file)
                print(f"wrinting : {arcname}\r",end="")
                z.write(path.join(root,file),arcname=arcname)
            
    psuccess(f"\nProject's archive created at : {dirpath}/{project_name}.zip")