import os
from  config import config
#from config.config import config_master
#from config.config import config_data
#from config import config_client
#from start import start 

def main_one():
    from installation import installation as inst
    os.system("clear")
    print( "\n\n\n\t\t\t\t\t\t\t\t\tWelcome\n\t\t\t__________________________________________________________________________________________________")


    print("\n\n\n\t\t\t\t\t\t\t\t\tMenu\n\t\t\t\t\t\t\t-------------------------------------")
    print("\n\t\t\t\t\t\t\t\t Enter 1 for  configure install hadoop and java jdk in your system /n")

    print("\n\t\t\t\t\t\t\t\t Enter 2 for  configure master node")
    print("\n\t\t\t\t\t\t\t\t Enter 3 for  configure data node")
    print("\n\t\t\t\t\t\t\t\t Enter 4 for  configure client node")
    print("\n\t\t\t\t\t\t\t\t Enter 5 for  start services")
    a=input("\n\t\t\t\t\t\t\t\tenter your choice")
    a=int(a)
    s=[2,3,4]
    if a in s:
        os.system("clear")
        inst()
    elif a==5:
        start_s()
    else:
        print("you know nothig john show")

