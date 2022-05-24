import os 
def installation():
    print("enter one hadoop installation /n enter 2 for java installation ")
    a=input("Enter here:")
    a=int(a)
    size=os.get_terminal_size()
    if a==1:
        os.system("wget https://archive.apache.org/dist/hadoop/core/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm")
        os.system("rpm -i hadoop-1.2.1-1.x86_64.rpm")
        installation_status="done"
        return installation_status
    if a==2:
        os.system("wget 35.244.242.82/yum/java/el7/x86_64/jdk-8u171-linux-x64.rpm")
        os.system("rpm -i jdk-8u171-linux-x64.rpm")
        input("press any key to continue")
        print("done")

print(installation)

