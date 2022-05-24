import os
import kuber_sertup
import laun_pod
import load_bal
import secret
import multiapp
print("Welcome to kuberates")
print("print1 for download and sertup  kubernates cluster in your device\npress2 for launching pod from  your cluseter\npress 3 for setup load balancer \npress 4 for create  deployment \npress 5 for setup  secret \npress6 for load multi node cluster \n press7 for setup a multitier application cluster")
a=input("Enter Your chocice  here")
if a =="1":
    setup()
elif a=="2":
    launching_pod()
elif a=="3":
    load_banacer()
elif a=="4":
    deploy()
elif a=="5":
    secret()
elif a=="6":
    multi_node_cluster()
elif a=="7":
    multi_tier()

    
