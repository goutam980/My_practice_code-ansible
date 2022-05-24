import  subprocess 
def ansi_inst():
    os.system("yum install ansible -y")
def ansi_load():
    group_name=input("enter you  group  name")
    ip=input("Enter you  ip addrs")
    pas=input("enter your password")
    subprocess.getoutput("echo [{}] >> /root/arth/myownapp/ansible/inventory.txt".format(group_name))
    subprocess.getoutput("echo {} ansible_ssh=root ansible_ssh_pass={} ansible_connection=ssh >> /root/arth/myownapp/ansible/inventory.txt".format(ip,pas))
    subprocess.getoutput("echo g_name: {} :: ,ip: {}, ::pass: {} >> /home/playbook/data1.txt".format(group_name,ip,pas))
    a= subprocess.getstatusoutput("ansible-playbook /root/arth/myownapp/ansible/load_balancer.yml")
    print(a)
ansi_load()

