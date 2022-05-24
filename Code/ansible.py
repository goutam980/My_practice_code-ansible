import os
import ansi 
#from config import config_client
#from start import start 

def ansible_main():
    from installation import installation as inst
    os.system("clear")
    print( "\n\n\n\t\t\t\t\t\t\t\t\tWelcome\n\t\t\t__________________________________________________________________________________________________")


    print("\n\n\n\t\t\t\t\t\t\t\t\tMenu\n\t\t\t\t\t\t\t-------------------------------------")
    print("\n\t\t\t\t\t\t\t\t Enter 1 for  config ansible in your system /n")
    print("\n\t\t\t\t\t\t\t\t Enter 2 for  add your manage nodes in  your inventory")
    print("\n\t\t\t\t\t\t\t\t Enter 3 for  show all thing you can do with ansible")
    print("\n\t\t\t\t\t\t\t\t Enter 4 for  search using ansible fact")
    print("\n\t\t\t\t\t\t\t\t Enter 5 for  notes of ansible")
    print("\n\t\t\t\t\t\t\t\t Enter 6 for  cheatsheet of ansible")
    print("\n\t\t\t\t\t\t\t\t Enter 6 for  exit")
    print("\n\t\t\t\t\t\t\t\t Enter 7 for  loadbalancer setup  on you own pc")


    a=input("\n\t\t\t\t\t\t\t\tenter your choice")
    a=int(a)

    if a==1:
        os.system("clear")
        ansi.ansi_inst()
    elif a==2:
        ansi.add_manage_node()
    elif a==3:
        ansi.ansi_task()
    elif a==4:
        ansi.ansi_search()
    elif a==5:
        ansi.ansi_notes()
    elif a==6:
        ansi.ansi_cheatsheet()
    elif a==7:
        ansi.ansi_load()
    elif a==8:
        ansi.ansi_exit()
    else:
        print("you know nothig john show")

                      
