import pyttsx3
import menu
import subprocess as sp
import os 
import ansible
import webbrowser as wb
import getcnt
from os import system, name 
#from colorama import Fore, Back, Style
#from getcnt import getcnt
import main_hadoop 



while True:
    print( "\n\n\n\t\t\t\t\t\t\t\t\tWelcome\n\t\t\t__________________________________________________________________________________________________")
    


    print("\n\n\n\t\t\t\t\t\t\t\t\tMenu\n\t\t\t\t\t\t\t-------------------------------------")
    print("\n\t\t\t\t\t\t\t\t1: Get connect to us ")
    print("\n\t\t\t\t\t\t\t\t2: Docker ")
    print("\n\t\t\t\t\t\t\t\t3: Amazon Web Services (AWS)") 
    print("\n\t\t\t\t\t\t\t\t4: Hadoop")
    print("\n\t\t\t\t\t\t\t\t5: ansible")
    print("\n\t\t\t\t\t\t\t\t6: Increase/Decrease the size of HD using LVM")
    print("\n\t\t\t\t\t\t\t\t7: Shut down/Restart") 
    print("\n\t\t\t\t\t\t\t\t8: Exit")
    #pyttsx3.speak("Please...Enter your..choice")
    ch=input("\n\n\t\t\t\t\t\t\t\tEnter your choice:")
    ch=int(ch)
    if(ch==1):
        getcnt.getcnt()
    elif(ch==2):
        menu.docker()
    elif(ch==3):
        menu.aws()
    elif(ch==4):
        os.system("clear")
        print("hello world")
        main_hadoop.main_one()
    elif(ch==5):
        os.system("clear")
        ansible.ansible_main()
    
    elif(ch==6):
        shut&res()
    elif(ch==7):
        exit()

