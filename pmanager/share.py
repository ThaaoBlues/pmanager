from flask import Flask, render_template, send_from_directory,send_file,request,redirect,flash
from pathlib import Path
from os import path
from pmanager.res import *
import flaskcode

#init flask app
app = Flask(__name__)
app.config.from_object(flaskcode.default_config)
app.register_blueprint(flaskcode.blueprint, url_prefix='/')



@app.route('/')
def hello():
    return "I show my presence, nothing more"


def initialize(namespace):

    project_name = namespace.project_name[0]


    #get project full path
    if not path.exists("config/default_path.conf"):
        dirpath = get_home_dir_path()+"/projects/"+project_name
    else:
        with open("config/default_path.conf","r",encoding="utf-8") as f:
            dirpath = f.read()+"/"+ project_name
    
    #put project full path into flaskcode variable
    app.config['FLASKCODE_RESOURCE_BASEPATH'] = dirpath


    pinfo(f"running web IDE on :\n {dirpath}")

    #loop until a correct port is typed or a keyboardInterrupt occurs
    while True:
        try:
            port = int(input("Select which port you want to run the web IDE\n-->"))
            break
        except Exception as e:
            if e.__class__.__name__ == "KeyboardInterrupt":
                return
            else:
                pwarn("Port must be an integer, retry now ;)\n")


    #run web server
    app.run(host="0.0.0.0",port=port)