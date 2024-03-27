import os
import json
import studentoptions


def studentportal(mainportal):
    os.system('cls')
    print("************************Student Portal***************************")
    print('1-Signup')
    print("2-login")
    print("3-Back")
    print("4-Exit")
    choice = int(input("Enter the choice:"))
    if choice == 1:
        signup()
    elif choice == 2:
        login()
    elif choice == 3:
        mainportal()
    elif choice == 4:
        exit()
    else:
        print("Invalid choice")


path = r".\studentlist.txt"


def signup():
    info = []
    name = str(input("Enter your name:"))
    Id = int(input("Enter your id:"))
    password = str(input("Create your password:"))
    if os.stat(path).st_size != 0:
        info = gettingdata()
    info.append({'name': name, 'Id': Id, 'password': password,
                 'blockstatus': "unblocked"})
    addingtofile(info)


def login():
    Id = int(input("Enter your id:"))
    password = str(input("Enter your password:"))
    if os.stat(path).st_size != 0:
        libdata = gettingdata()
        for data in libdata:
            if data['Id'] == Id and data['password'] == password:
                studentoptions.studentoptions()
        # else:
        #     print("Invalid credentials")
    else:
        print("not found")


def addingtofile(info):
    file = open(path, 'w')
    f = file.write(json.dumps(info))
    file.close()


def gettingdata():
    file = open(path, 'r')
    data = eval(file.read())
    file.close()
    return data
