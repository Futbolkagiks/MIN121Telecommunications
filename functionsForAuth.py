from functionsForAuth import *
from typing import Tuple
from openpyxl import load_workbook
import openpyxl
workbook= load_workbook(filename="Users.xlsx")
EmployeesSheet=workbook["Employees"]
ClientsSheet=workbook["Clients"]

def login_check(account,type):
    LoginCheck=False
    for col in type["B"]:
        if col.value==account[0]:
            LoginCheck=True
    if LoginCheck==False:
        return False
    elif LoginCheck==True:
        return True

def account_new():
    if input("Enter who you wish to be Cleint/Employee: ")=="Employee":
        account_type=EmployeesSheet
    else:
        account_type=ClientsSheet
    new_account=((input("Enter name: ")),(input("Enter login: ")),(input("Enter password: ")))
    while login_check(new_account[1],account_type)==True:
        print("The login you typed in is already being used, try again")
        new_account[1]=input("Enter another login: ")
    account_type.append(new_account)
    workbook.save("Users.xlsx")
    print("You have been registered")

def account_auth():
    while True:
        chat = input("Type in E if you are an employee or C for Client: ")
        if chat=="E":
            account_type=EmployeesSheet
            break
        elif chat=="C":
            account_type=ClientsSheet
            break
    CHECK1=False
    CHECK2=False
    while CHECK1==False and CHECK2==False:
        account=((input("Enter login: ")),(input("Enter password: ")))
        if account_type==EmployeesSheet:
            for col in EmployeesSheet["B"]:
                if col.value==account[0]:
                    CHECK1=True
            for col in EmployeesSheet["C"]:
                if col.value==account[1]:
                    CHECK2=True
        elif account_type==ClientsSheet:
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
