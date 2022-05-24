import os 
print("Welcome in  kubernates setup for setup:")
c_ip=input("Enter the ip of your system where you want to setup client:")
mas_ip=input("Enter the ip where you want your master node:")
work_c=input("Enter here how muchworker node you want")

#client node


#master node 

s=os.system("sh root@{}".format(mas_ip))
if s:
    os.system("curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64")
    os.system("sudo install minikube-linux-amd64 /usr/local/bin/minikube")

   

#worker node
w_c=int(work_c)

total_client=[]
for i in range(w_c):
    i=input("Enter your worker node ip")
    total_client.append(i)
for j in range(len(total_client)):
    print(total_client[j])

