import os
import json
import options


def librarianportal(mainportal):
    os.system('cls')
    print("************************Librarian Portal***************************")
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


path = r".\librarian.txt"


def signup():
    info = []
    name = str(input("Enter your name:"))
    Id = int(input("Enter your id:"))
    password = str(input("Create your password:"))
    if os.stat(path).st_size != 0:
        info = gettingdata()
    info.append({'name': name, 'Id': Id, 'password': password,
                'status': 'not approved'})
    addingtofile(info)


def login():
    Id = int(input("Enter your id:"))
    password = str(input("Enter your password:"))
    libdata = gettingdata()
    for data in libdata:
        if data['Id'] == Id and data['password'] == password and data['status'] == 'approved':
            lists()
        elif data['Id'] == Id and data['password'] == password and data['status'] != 'approved':
            print("Not yet approved please wait")
    # else:
    #     print("Invalid credentials")


def addingtofile(info):
    file = open(path, 'w')
    f = file.write(json.dumps(info))
    file.close()


def gettingdata():
    file = open(path, 'r')
    data = eval(file.read())
    file.close()
    return data


def lists():
    dict = {1: addbooks, 2: viewbooks, 3: editbooks,
            4: viewstudents, 5: approvebooks, 6: returnapprove}
    os.system('cls')
    print("************************librariyan Portal***************************")
    print("1-Add books")
    print("2-View books")
    print("3-Edit books")
    print("4-View students")
    print("5-Approve books")
    print("6-Return approve")

    choice = int(input("Enter your choice:"))
    dict[choice]()


def addbooks():
    options.addbooks()


def viewbooks():
    options.viewbooks()


def editbooks():
    options.editbooks()


def viewstudents():
    options.viewstudents()


def approvebooks():
    data = options.approvebooks()


def returnapprove():
    options.returnapprove()
