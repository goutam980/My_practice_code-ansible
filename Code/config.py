import os

def config():
    def config_master():
        x=1
        while x==1:
            os.system("clear")
            print("Enter 1 for  setup datanode \nEnter 2 for formatdatanode\nEnter 3 for start datanode\nEnter 4 for stop datanode\nEnter 5 for go to hadoop  menu ")
            a=input("Enter your choice here")
            a=int(a)
            if a==1:
                os.system("clear")
                fna=input("Enter datanode directory name here")
                ip = input("Enter the IP address of Name-node")
                port = int(input("Enter the port number"))
                datafile1 = f"""<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>/{fna}</value>\n</property>\n</configuration>\n"""
                datafile2 = f"""<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{ip}:{port}</value>\n</property>\n</configuration>\n"""
                hdfs=open("/etc/hadoop/hdfs-site.xml","w")
                os.system("mkdir {}".format(fna))
                if hdfs:
                    hdfs.writelines(datafile1)
                    print("all set now your hdfs fle created sucessfully")
                    input("press enter for continue")

                    hdfs.close()
                
                core=open("/etc/hadoop/core-site.xml","w")
                if core:
                    core.writelines(datafile2)
                    print("done your file sucessfully created")
                    input("press enter for continue")

                    core.close()
            if a==2:
                os.system("hadoop datanode -format")
                print("your datanode has been sucssfully formated")
                input("press enter for continue")

            if a==3:
                os.system("hadoop-daemon.sh start datanode")
                print("your datanode has been sucssfully started")
                input("press enter for continue")
            if a==4:
                os.system("hadoop-daemon.sh stop datanode")
                print("your datanode has been sucssfully stopped")
                input("press enter for continue")


               







        return "thing is in  progress "
    def config_client():
        y = 1
        while y == 1:
            print("Enter 1 to setup Client-node")
            print("Enter 2 to change block-size and replication-factor")
            print("Enter 3 to see the files in hadoop cluster")
            print("Enter 4 upload the file in hadoop cluster")
            print("Enter 5 to remove the file from hadoop")
            print("Enter 6 to see a file in hadoop cluster")
            print("Enter b to go back to Hadoop menu")

            c = input("Enter your choice here: ")

            if c == "1":
                ip = input("Enter the IP address of Name-node: ")
                port = int(input("Enter the port number: "))

                datafile5 = f"""<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{ip}:{port}</value>\n</property>\n</configuration>\n"""

                corefile = open("/etc/hadoop/core-site.xml", "w")
                if corefile:
                    print("core-site.xml created succesfully ..... now writing in file.....\n")
                    corefile.writelines(datafile5)
                    print("core-site.xml written successfully..... now closing file")
                    corefile.close()
                    print("Hadoop Client-node setup successful")

            elif c == "2":
                replication_factor = input("Enter the Replication-factor: ")
                block_size = input("Enter the block-size in bytes: ")

                datafile6 = f"""<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<configuration>\n<property>\n<name>dfs.replication</name>\n<value>{replication_factor}</value>\n</property>\n<property>\n<name>dfs.block.size</name>\n<value>{block_size}</value>\n</property>\n</configuration>\n"""

                hdfsfile = open("/etc/hadoop/hdfs-site.xml", "w")
                if hdfsfile:
                    print("hdfs-site.xml created succesfully ..... now writing in file.....\n")
                    hdfsfile.writelines(datafile6)
                    print("hdfs-site.xml written successfully..... now closing file")
                    hdfsfile.close()

            elif c == "3":
                os.system("hadoop fs -ls /")

            elif c == "4":
                name = input("Enter the name of the file: ")
                os.system(f"hadoop.fs -put {name} /")

            elif c == "5":
                name = input("Enter the name of the file you want to remove: ")
                os.system(f"hadoop.fs -rm /{name}")

            elif c == "6":
                name = input("Enter the name of the file you want to see: ")
                os.system(f"hadoop.fs -cat /{name}")

            elif c == "b":
                y = 0
                if c != "b":
                    input("press any key to continue")
                    os.system("tput clear")

        
        else:
            print("Invalid request")
            os.system("tput clear")





    def onfig_client():
        y = 1
        while y == 1:


            print("Enter 1 to setup Client-node")
            print("Enter 2 to change block-size and replication-factor")
            print("Enter 3 to see the files in hadoop cluster")
            print("Enter 4 upload the file in hadoop cluster")
            print("Enter 5 to remove the file from hadoop")
            print("Enter 6 to see a file in hadoop cluster")
            print("Enter b to go back to Hadoop menu")
            
            
            a_client=input("enter here")
            a_client=int(a_client)
            #a_client=int(a_client)
            if a_client==1:
                os.system("clear")
                ip = input("Enter the IP address of Name-node")
                port =input("Enter the port number")
                port=int(port)

                datafile5 = f"""<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{ip}:{port}</value>\n</property>\n</configuration>\n"""
                core=open("/etc/hadoop/core-site.xml","w")
                if hdfs:
                    hdfs.writelines(datafile5)
                    print("all set now your hdfs fle created sucessfully")
                    input("press enter for continue")
                    core.close()
           
            elif a_client==2:
                ss=input=("hi please provide replication factor")
                iput=("enter size in bytes")
                datafile6 = f"""<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<configuration>\n<property>\n<name>dfs.replication</name>\n<value>{ss}</value>\n</property>\n<property>\n<name>dfs.block.size</name>\n<value>{iput}</value>\n</property>\n</configuration>\n"""
                core=open("/etc/hadoop/hdfs-site.xml","w")
                if core:
                    core.writelines(datafile6)
                    print("done your file sucessfully created")
                    input("press enter for continue")
                    core.close()
            elif a_client == "3":
                os.system("hadoop fs -ls /")

            elif a_client == "4":
                name = input("Enter the name of the file: ")
                os.system(f"hadoop.fs -put {name} /")

            elif a_client == "5":
                name = input("Enter the name of the file you want to remove: ")
                os.system(f"hadoop.fs -rm /{name}")

            elif a_client == "6":
                name = input("Enter the name of the file you want to see: ")
                os.system(f"hadoop.fs -cat /{name}")

            elif a_client == "b":
                y = 0
                if c != "b":
                    input("press any key to continue")
                    os.system("tput clear")
        else:
            print("Invalid request")
        os.system("tput clear")




                     
                        




    def config_data():
        y = 1
        while y == 1:
            print("Enter 1 to setup Data-node")
            print("Enter 2 to start Data-node")
            print("Enter 3 to stop Data-node")
            print("Enter 4 to format Data-node")
            print("Enter b to go back to Hadoop menu")

            d = input("enter your choice here: ")

            if d == "1":
                ip = input("Enter the IP address of Name-node")
                port = int(input("Enter the port number"))

                datafile1 = """<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>/datade</value>\n</property>\n</configuration>\n"""

                datafile2 = f"""<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{ip}:{port}</value>\n</property>\n</configuration>\n"""
                hdfsfile = open("/etc/hadoop/hdfs-site.xml", "w")
                os.system("mkdir /datanode")
                if hdfsfile:
                    print("hdfs-site.xml created succesfully ..... now writing in file.....\n")
                    hdfsfile.writelines(datafile1)
                    print("hdfs-site.xml written successfully..... now closing file")
                    hdfsfile.close()
                    corefile = open("/etc/hadoop/core-site.xml", "w")
                    if corefile:
                        print("core-site.xml created succesfully ..... now writing in file.....\n")
                        corefile.writelines(datafile2)
                        print("core-site.xml written successfully..... now closing file")
                        corefile.close()
                        print("Hadoop Data-node setup successful")

            elif d == "2":
                os.system("hadoop-daemon.sh start datanode")
                print("Data-node started..")

            elif d == "3":
                os.system("hadoop-daemon.sh stop datanode")
                print("Data-node stopped..")

            elif d == "4":
                os.system("hadoop datanode -format")
                print("Data-node formatted..")

            elif d == "b":
                y = 0
                if d != "b":
                    input("press any key to continue")
                    os.system("tput clear")


    
    y=1
    while y==1:
        print("Enter 1 for config master node \nEnter 2 for config client node \nEnter 3 for for config data node\nEnter 4 for exit")
        aa=input("Enter your choice here :")
        aa=int(aa)
        if(aa==1):
            config_master()
            print(config_master())
        elif(aa==2):
            config_client()
            print(config_client())
        elif(aa==3):
            config_data()
            print(config_data())
        elif(aa==4):
            print("Thanks")
            y=0
        else:
            print("print x for exit")
            ab=input("enter here")
            if ab=="x":
                y=0

