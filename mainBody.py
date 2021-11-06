from typing import Tuple
from openpyxl import load_workbook
import openpyxl
workbook= load_workbook(filename="Users.xlsx")
EmployeesSheet=workbook["Employees"]
ClientsSheet=workbook["Clients"]

def account_new():
    new_account=((input("Enter name: ")),(input("Enter login: ")),(input("Enter password: ")))
    if input("Enter who you wish to be Cleint/Employee: ")=="Employee":
        EmployeesSheet.append(new_account)
    else:
        ClientsSheet.append(new_account)
    workbook.save("Users.xlsx")
    print("You have been registered")

def account_auth():
    typecheck=False
    while typecheck==False:
        type=input("Type in E if you are an employee or C for Client: ")
        typecheck=True
    CHECK1=False
    CHECK2=False
    while CHECK1==False and CHECK2==False:
        account=((input("Enter login: ")),(input("Enter password: ")))
        if type.upper()=="E":
            for col in EmployeesSheet["B"]:
                if col.value==account[0]:
                    CHECK1=True
            for col in EmployeesSheet["C"]:
                if col.value==account[1]:
                    CHECK2=True
        elif type.upper()=="C":
            for col in ClientsSheet["B"]:
                if col.value==account[0]:
                    CHECK1=True
            for col in ClientsSheet["C"]:
                if col.value==account[1]:
                    CHECK2=True
        elif CHECK1==False or CHECK2==False:
            print("Try again")
            continue
    print("Success")

print("WELCOME")
q = input('To enter the program, write AUTH. If you are a new user, write NEW. If you wish to stop the programm, write EXIT: ')
if q=="AUTH":
    account_auth()
elif q=="NEW":
    account_new()

