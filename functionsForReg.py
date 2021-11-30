from typing import *
from openpyxl import *
import pandas as pd

workbook= load_workbook(filename="Users.xlsx")
EmployeesSheet=workbook["Employees"]
ClientsSheet=workbook["Clients"]

def login_check_2(new_account,type):
    while True:
        LoginCheck=False
        for col in type.iter_rows(min_row=2,max_col=4,min_col=3,values_only=True):
            if new_account[1]==col[0]:
                LoginCheck=True
        if LoginCheck==True:
            print("The login you typed in is already being used, try again")
            new_account[1]=input("Enter another login: ")
        else:
            break

def create_User(account_type):
    print("Welcome to registration screen!")
    new_account=[int(len(account_type["A"])),(input("Enter name: ")),(input("Enter login: ")),(input("Enter password: "))]
    login_check_2(new_account,account_type)
    account_type.append(new_account)
    workbook.save("Users.xlsx")
    print("User has been registered")
    return





