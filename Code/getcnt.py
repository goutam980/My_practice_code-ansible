import os 
def getcnt():

    print("To get connected you have to do some step after those step we can connect to you and setup your   pc")
    a=input("press 1 for get connected")
    if(a =="1"):
        os.system("systemctl stop firewalld")
        os.system("setenforce 0")
        ip=input("enter your ip here ")
    




