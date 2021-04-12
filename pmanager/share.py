from flask import Flask, render_template, send_from_directory,send_file,request,redirect,flash
from pathlib import Path
from os import path
from pmanager.res import *

#init flask app
app = Flask(__name__)


#home
@app.route("/")
def home():
    print("dirpath : "+ read_temp_file("dirpath"))
    filesname = list(Path(read_temp_file("dirpath")).rglob("*.*"))
    for i in range(len(filesname)):
        filesname[i] = str(filesname[i]).replace("WindowsPath('","").replace("')","")
    print(filesname)

    filescontent = []
    for file in filesname:
        with open(path.join(read_temp_file("dirpath"),file),"r",encoding="utf-8", errors='ignore') as f:
            filescontent.append(f.read().replace("\n","<br>").replace("    ","&nbsp&nbsp&nbsp&nbsp"))
            f.close()

    return render_template("index.html",filesname=filesname,lenght=len(filesname),filescontent=filescontent)



def initialize():
    app.run(host="0.0.0.0",port=80)