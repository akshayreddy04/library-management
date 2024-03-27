import os
import librariyan
import json
import options


def adminportal(mainportal):
    dict = {1: addbooks, 2: viewbooks, 3: editbooks,
            4: viewstudents, 5: blockedstudets, 6: librarianapprovals, 8: exitprogram}
    os.system('cls')
    print("************************Admin Portal***************************")
    allow = check()
    if allow:
        os.system('cls')
        print("************************Admin Portal***************************")
        print("1-Add books")
        print("2-View books")
        print("3-Edit books")
        print("4-View students")
        print("5-Blocked studets")
        print("6-Librarian approvals")
        print("7-back")
        print("8-exit")
        choice = int(input("Enter your choice:"))
        if choice == 7:
            options.back(mainportal)
        else:
            dict[choice]()
            print(dict[choice])


def check():
    username = "admin"
    password = 123
    user = str(input("Enter the username:"))
    Id = int(input("Enter the password:"))
    if user == username and Id == password:
        return True
    else:
        print("Invalid credentials")
        return False


def addbooks():
    options.addbooks(adminportal)


def viewbooks():
    options.viewbooks(adminportal)


def editbooks():
    options.editbooks(adminportal)


def viewstudents():
    options.viewstudents(adminportal)


def blockedstudets():
    options.unblockstudents(adminportal)


def exitprogram():
    exit()


def librarianapprovals():
    libdata = librariyan.gettingdata()
    i = 1
    for data in libdata:
        print("{}. Name:{}  Id:{}  Status:{}".format(
            i, data['name'], data['Id'], data['status']))
        i += 1
    choice = int(input("Enter the sl.no of the librarian to approve:"))
    approve(choice)


def approve(libnum):
    data = librariyan.gettingdata()
    data[libnum-1]['status'] = "approved"
    librariyan.addingtofile(data)
