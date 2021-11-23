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
        global account_type
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
        for col in account_type["B"]:
            if col.value==account[0]:
                global row
                row=col
                CHECK1=True
        for col in account_type["C"]:
            if col.value==account[1]:
                CHECK2=True
        print("Try again")
    print("Success")

