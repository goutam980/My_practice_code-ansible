from  flask  import Flask
from flask import request
from  flask import render_template
import subprocess


app=Flask("mylbapp")
@app.route("/",methods=['GET'])
def name():
    a="hi bhaoi"
    return render_template("home.html")

@app.route("/home",methods=['GET'])
def home():
    g_name=request.args.get('x')
    ip=request.args.get('y')
    request.args.get('z')
    passwd=render_template("home.html")
    subprocess.getoutput("echo [{}] >> /root/arth/myownapp/ansi_f/ip.txt".format(g_name))

    ab=subprocess.getoutput("echo {} ansible_ssh=root ansible_ssh_pass={} ansible_connection=ssh >> /root/arth/myownapp/ansi_f/ip.txt".format(ip,passwd))

    return render_template("name.html")

@app.route("/pl",methods=['GET'])
def pl():
    return render_template("name.html")



@app.route("/play",methods=['GET'])
def docker():
    #a=subprocess.getoutput("curl 192.168.43.207:8899/home.html")
    compleat=" please wait your  setup is loading "
    play=request.args.get('g')
    """if play=="load balancer":

        ast=subpocess.getoutput("ansible-playbook 1Load_bal.yml ")
    
    """
    a="192.168.43.207:8899/home.html"
    ast=subprocess.getoutput("ansible-playbook docker_c.yml ")
    return render_template("final.html",mn=ast,a=a)

    
