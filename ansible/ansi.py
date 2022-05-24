import  subprocess 
def ansi_inst():
    os.system("yum install ansible -y")
def ansi_load():
    print("Enter 1 fo new group \nEnter 2 for choosing older group  ")
    a=input("Enter here")
    if a=="1":
        group_name=input("enter you  group  name")
        subprocess.getoutput("echo [{}] >> /root/arth/myownapp/ansible/inventory.txt".format(group_name))
        user_count=input("how much  ip  you want to  add")
        ucount =int(user_count)
        for i in range(ucount):
            ip=input("Enter you  ip addrs")
            pas=input("enter your password")
            subprocess.getoutput("echo {} ansible_ssh=root ansible_ssh_pass={} ansible_connection=ssh >> /root/arth/myownapp/ansible/inventory.txt".format(ip,pas))
            subprocess.getoutput("echo g_name: {} :: ,ip: {}, ::pass: {} >> /home/playbook/data1.txt".format(group_name,ip,pas))
    elif a=="2":
        av=input("enter you playbook name")
        asp=subprocess.getstatusoutput("ansible-playbook {}".format(av))
        print(asp)
   
ansi_load()

