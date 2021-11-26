from typing import *
from openpyxl import *
workbook= load_workbook(filename="Users.xlsx")
EmployeesSheet=workbook["Employees"]
ClientsSheet=workbook["Clients"]

def login_check(account,type):
    LoginCheck=False
    for col in type["C"]:
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
    new_account=(int(len(account_type["A"])-1),(input("Enter name: ")),(input("Enter login: ")),(input("Enter password: ")))
    while login_check(new_account[1],account_type)==True:
        print("The login you typed in is already being used, try again")
        new_account[1]=input("Enter another login: ")
    account_type.append(new_account)
    workbook.save("Users.xlsx")
    print("You have been registered")




