import options
import os
import json
from datetime import datetime, timedelta
path1 = r".\books.txt"
path2 = r".\request.txt"
current_date = datetime.now().date()
date_string = current_date.strftime('%Y-%m-%d')


def studentoptions():
    os.system('cls')
    print("************************Student Portal***************************")
    print("1.View books")
    print("2.Return request")
    choice = int(input("Enter your choice:"))

    if choice == 1:
        viewbooks()
    elif choice == 2:
        returnrequest()
    else:
        print("Invalid choice")


def viewbooks():
    info = []
    searcheddata = search()
    print("Do you want to raise request for this book")
    print("1.Yes")
    print("2.no")
    choice = int(input("Enter the num:"))
    if choice == 1:
        if searcheddata['quantity'] != 0:
            Id = int(input("Enter your id:"))
            checkblock = checkblockstatus(Id)
            print(checkblock)
            if checkblock == True:
                searcheddata['studentid'] = Id
                searcheddata['request'] = "approverequest"
                if os.stat(path2).st_size != 0:
                    info = requestdata(path2)
                info.append(searcheddata)
                adddata(info, path2)
            else:
                print(
                    "Sorry we can't raise your request because your are blocked ,contact admin for further information ")
        else:
            availability(searcheddata)
    elif choice == 2:
        print()
    else:
        print("Invalid choice")


def returnrequest():
    list = []
    Id = int(input("Enter your Id:"))
    if os.stat(path2).st_size != 0:
        data = requestdata(path2)
    i = 0
    for val in data:
        if val['studentid'] == Id and val['request'] == "approved":
            i += 1
            list.append(val)
            print(i, val)
    if i > 0:
        choice = int(input("Enter the num of book to return:"))
        difference = differenceofdate(data[choice-1]['date'])
        if difference > 90:
            block(Id)
            print(
                "sorry you can't raise request because you are blocked,contact admin for further information")
        else:
            if checkblockstatus(Id) == True:
                sendreturnrequest(list[choice-1])
            else:
                print(
                    "sorry you can't raise request because you are blocked,contact admin for further information")


def requestdata(path):
    file = open(path, 'r')
    data = eval(file.read())
    file.close()
    return data


def adddata(info, path):
    file = open(path, 'w')
    f = file.write(json.dumps(info))
    file.close()


def search():
    dict = {1: "bookname", 2: "author", 3: "category:", 4: "quantity"}
    print("1.Bookname")
    print("2.Author name")
    print("3.branch")
    print("4.quantity")
    choice = int(input("Enter the no to search:"))
    print("Enter the ", dict[choice])
    if choice < 4 and choice > 0:
        searchdata = str(input())
    elif choice == 4:
        searchdata = int(input())
    else:
        print("Invalid choice")
    listsearch = []
    listfullsearch = []
    data = options.getdata(path1)

    for val in data:
        if searchdata in val[dict[choice]]:
            listsearch.append(val[dict[choice]])
            listfullsearch.append(val)
    i = 1
    for values in listsearch:
        print(i, values)
        i += 1
    choose = int(input("enter the no for details:"))
    print(listfullsearch[choose-1])
    return listfullsearch[choose-1]


def differenceofdate(date):
    previous_date = datetime.strptime(date, "%Y-%m-%d").date()
    date_difference = current_date - previous_date
    days_difference = date_difference.days
    return days_difference


def checkblockstatus(Id):
    path3 = r".\studentlist.txt"
    if os.stat(path3).st_size != 0:
        data = options.getdata(path3)
        for val in data:
            if val['Id'] == Id and val['blockstatus'] == "blocked":
                return False
        return True
    else:
        print("no data")


def block(Id):
    path3 = r".\studentlist.txt"
    if os.stat(path3).st_size != 0:
        data = options.getdata(path3)
        for val in data:
            if val['Id'] == Id:
                val['blockstatus'] = "blocked"


def sendreturnrequest(returnbook):
    print(returnbook)
    if os.stat(path2).st_size != 0:
        data = options.getdata(path2)
        for val in data:
            if val == returnbook:
                val['request'] = "returnrequest"
                print(val)
        options.addtofile(data, path2)


def availability(searcheddata):
    list = []
    if os.stat(path2).st_size != 0:
        data = options.getdata(path2)
    for val in data:
        if val['bookname'] == searcheddata['bookname'] and val['request'] == "approved":
            list.append(val['date'])
    dates = [datetime.strptime(date.strip(), "%Y-%m-%d") for date in list]
    oldest_date = min(dates)
    newdate = oldest_date+timedelta(days=90)
    print("The book will be available from ", newdate.strftime("%Y-%m-%d"))
