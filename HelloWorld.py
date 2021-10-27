from openpyxl import load_workbook
import openpyxl
workbook= load_workbook(filename="Users.xlsx")
EmployeesSheet=workbook["Employees"]
ClientsSheet=workbook["Clients"]

def account_new():
    login_new = input("Enter new login: ")
    password_new = input("Enter new password: ")
    if input("Enter who you wish to be Cleint/Employee: ")=="Employee":
        EmployeesSheet["B"]=login_new
        EmployeesSheet["C"]=password_new
    else:
        ClientsSheet["B"]=login_new
        ClientsSheet["C"]=password_new
    print("You have been registered")


def account_auth():
    login_auth = input("Enter the login: ")
    password_auth = input("Enter the password: ")
    login_found=False
    password_found=False
    if input("Enter who you are Client/Employee: ")=="Employee":
        for col in EmployeesSheet["B"]:
            if col.value==login_auth:
                login_found=True
        for col in EmployeesSheet["C"]:
            if col.value==password_auth:
                password_found=True
    else:
        for col in ClientsSheet["B"]:
            if col.value==login_auth:
                login_found=True
        for col in ClientsSheet["C"]:
            if col.value==password_auth:
                password_found=True
    if login_found==True and password_found==True:
        print("Welcome")
    else:
        print("Wrong Login or Password")

print("WELCOME")
q = input('To enter the program, write AUTH. If you are a new user, write NEW. If you wish to stop the programm, write EXIT: ')
if q=="AUTH":
    account_auth()
elif q=="NEW":
    account_new()

