import os 
print("Press 1 for maual partition \nPress 2 for lvm partation \nTo create lv press1")
a=input("enter here..")
a=int(a)
def manual():
    pass
def lvm_part():
    print(" press1 for checking disk name \nPress 2 to insert disk name ")
    av = input("enter here....")
    av=int(av)
    if av==1:
        a=os.system("fdisk -l")
        print(a)
    disk_name1=input("enter Your disk name here for lvm partation")
    print(os.system("pvcreate {}".format(disk_name1)))
    disk_name2=input("enter Your disk name here for lvm partation")
    print(os.system("pvcreate {}".format(disk_name2)))
    vgname=input("Enter your vg name here")
    print(os.system("vgcreate {0} {1} {2} ".format(vgname , disk_name1 , disk_name2))) 
    print(os.system("vgdisplay {}".format(vgname)))
    b=input("To create lv press1")

    if b=="1":
        size1=input("enter size of disk  in gb")
        name_of_lv=input("enter  the name of lv ")
        size=("{}G".format(size1))
        print(size)
        print(os.system("lvcreate --size {} --name {} ".format(size,name_of_lv)))
        print(os.system("lvdisplay {}".format(name_of_lv)))




if a==1:
    print("manual partation")
    manual()
else:
    print("lvm partation")
    lvm_part()
   
