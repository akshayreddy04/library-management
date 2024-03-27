import admin
import librariyan
import student


def mainportal():
    print("**********************Library Portal********************************")
    print("1-Admin portal")
    print("2-librarian portal")
    print("3-student portal")
    print("4-Exit")
    choice = int(input("Enter your portal:"))
    if choice == 1:
        admin.adminportal(mainportal)
    elif choice == 2:
        librariyan.librarianportal(mainportal)
    elif choice == 3:
        student.studentportal(mainportal)
    elif choice == 4:
        exit()
    else:
        print("Invalid choice")


mainportal()
