import os 
print("Press 1 for maual partition \nPress 2 for lvm partation")
a=input("enter here..")
a=int(a)
def manual():
    pass
def lvm_part():
    def menu_lvm():
        menu=print(" press1 for checking disk name \nPress 2 to create pv \nTo create vg press3,\nTo diaplay vg press4,\nTo create lv press5,\nTo display lv press6")
        av = input("enter here....")
    
        if av=="1":
            a=os.system("fdisk -l")
            print(a)
        elif av=='2':
            pv_create()

        elif av=="3":


            vg_create()
        elif av=="4":
            vg_create()
        elif av=="5":
            lv_create()
        elif av=="6":
            lv_create()
            


    def vg_create():
        disk_name1=input("enter Your disk name here for lvm partation")
        print(os.system("pvcreate {}".format(disk_name1)))
        
        disk_name2=input("enter Your disk name here for lvm partation")
        print(os.system("pvcreate {}".format(disk_name2)))
        a=input("1 for create 2 for display")
        if a=="1":
            vgname=input("Enter your vg name here")
            print(os.system("vgcreate {0} {1} {2} ".format(vgname , disk_name1 , disk_name2))) 
        elif a=="2":
            a=input("enter your vg name here")
            print(os.system("vgdisplay {}".format(a)))
        menu_lvm()
    
    def lv_create():
        a=input("1 for display 2 for create" )

        if a=="2":
            b=input("To create lv press1")
            size1=input("enter size of disk  in gb")
            name_of_lv=input("enter  the name of lv ")
            vg_name=input("enter name of your vg")
            size=("{}G".format(size1))
            print(size)
            print(os.system("lvcreate --size {} --name {} {} ".format(size,name_of_lv,vg_name)))
        elif a=="1":
            print(os.system("lvdisplay dev/{}/{}".format(vg_name,name_of_lv)))

    menu_lvm()


if a==1:
    print("manual partation")
    manual()
else:
    print("lvm partation")
    lvm_part()
   
