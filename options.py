import os
import json
from datetime import datetime
path1 = r".\books.txt"
path2 = r".\studentlist.txt"
path3 = r".\request.txt"
current_date = datetime.now().date()
date_string = current_date.strftime('%Y-%m-%d')


def addbooks(portal):
    info = []
    bookname = str(input("Enter the  bookname:"))
    author = str(input("Enter the author name:"))
    category = str(input("which branch it belongs to:"))
    quantity = int(input("Enter the quantity:"))
    if os.stat(path1).st_size != 0:
        info = getdata(path1)
    info.append({'bookname': bookname, 'author': author, 'category': category,
                'quantity': quantity})
    addtofile(info, path1)


def viewbooks(portal):
    if os.stat(path1).st_size == 0:
        print("No data")
    else:
        bookdata = getdata(path1)
        i = 1
        for data in bookdata:
            print("{}. Bookname:{}  Author:{} Category:{}  quantity:{}".format(
                i, data['bookname'], data['author'], data['category'], data['quantity']))
            i += 1


def editbooks(portal):
    dict = {1: "bookname", 2: "author", 3: "category:", 4: "quantity"}

    if os.stat(path1).st_size == 0:
        print("No data")
    else:
        viewbooks()
        choice = int(input("Enter the no of book to edit:"))
        print("1.Bookname")
        print("2.Author name")
        print("3.branch")
        print("4.quantity")
        subchoice = int(input("Enter the no to edit:"))
        print("Enter the ", dict[subchoice])
        if subchoice < 4 and subchoice > 0:
            editdata = str(input())
        elif subchoice == 4:
            editdata = int(input())
        else:
            print("Invalid choice")
        data = getdata(path1)
        data[choice-1][dict[subchoice]] = editdata
        addtofile(data, path1)


def viewstudents(portal):
    path2 = r".\studentlist.txt"
    if os.stat(path2).st_size == 0:
        print("No data")
    else:
        studentdata = getdata(path2)
        i = 1
        for data in studentdata:
            print("{}. Name:{}  Id:{}  Blockstatus:{}".format(
                i, data['name'], data['Id'], data['blockstatus']))
            i += 1


def approvebooks(portal):
    if os.stat(path3).st_size == 0:
        print("No data")
    else:
        data = getdata(path3)
        list = []
        i = 0
        for val in data:
            if val['request'] == "approverequest":
                list.append(val)
                i += 1
                print(i, val)
        if i > 0:
            accept = int(input("Enter the num to accept:"))
            for val in data:
                if val['studentid'] == list[accept-1]['studentid'] and val['bookname'] == list[accept-1]['bookname']:
                    val['request'] = "approved"
                    val['date'] = date_string
            addtofile(data, path3)
            decreasequantity(list[accept-1])
        else:
            print("No books to approve")


def returnapprove(portal):
    if os.stat(path3).st_size == 0:
        print("No data")
    else:
        data = getdata(path3)
        list = []
        i = 0
        for val in data:
            if val['request'] == "returnrequest":
                list.append(val)
                i += 1
                print(i, val)
        if i > 0:
            accept = int(input("Enter the num to accept:"))
            for val in data:
                if val['studentid'] == list[accept-1]['studentid'] and val['bookname'] == list[accept-1]['bookname']:
                    val['request'] = "returned"
                    val['datereturned'] = date_string
            addtofile(data, path3)
            increasequantity(list[accept-1])
        else:
            print("No books to approve")


def unblockstudents(portal):
    list = []
    if os.stat(path2).st_size != 0:
        data = getdata(path2)
        i = 0
        for val in data:
            if val['blockstatus'] == "blocked":
                i += 1
                list.append(val)
                print(i, val)
        if i > 0:
            choice = int(input("Enter the no of student to be unblocked:"))
            for val in data:
                if val == list[choice-1]:
                    print(1234)
                    val['blockstatus'] = "unblocked"
            addtofile(data, path2)
        else:
            print("no one are blocked")


def getdata(path):
    file = open(path, 'r')
    data = eval(file.read())
    file.close()
    return data


def addtofile(info, path):
    file = open(path, 'w')
    f = file.write(json.dumps(info))
    file.close()


def increasequantity(bookcredentials):
    data = getdata(path1)

    for val in data:
        if val['bookname'] == bookcredentials['bookname']:
            val['quantity'] += 1
    addtofile(data, path1)


def decreasequantity(bookcredentials):
    data = getdata(path1)
    print(bookcredentials['bookname'])
    for val in data:
        if val['bookname'] == bookcredentials['bookname']:
            print(type(val['quantity']))
            val['quantity'] -= 1
    addtofile(data, path1)


def back(portal):
    os.system('cls')
    portal()
