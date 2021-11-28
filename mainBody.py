from functionsForReg import *
from menu import *
from typing import *
from openpyxl import *
from colorama import init, Fore, Back, Style
workbook=load_workbook(filename="Users.xlsx")
EmployeesSheet=workbook["Employees"]
ClientsSheet=workbook["Clients"]
VVX=load_workbook(filename="Tariffs.xlsx")
Tariffs=VVX["Tariffs"]

def account_auth():
    global account_type
    print("Authentication")
    while True:
        chat = input("Type in E if you are an Employee or C for Client: ")
        if chat=="E":
            account_type=EmployeesSheet
            break
        elif chat=="C":
            account_type=ClientsSheet
            break
    CHECK1=False
    CHECK2=False
    while (CHECK1==False) and (CHECK2==False): #Разобраться с CHECK2
        account=((input("Enter login: ")),(input("Enter password: ")))
        for col in account_type.iter_rows(min_col=3,max_col=7,min_row=2,values_only=True):
            if col[0]==account[0]:
                print(CHECK1,CHECK2)
                CHECK1=True
                print(CHECK1,CHECK2)
            if col[1]==account[1]:
                print(CHECK1,CHECK2)
                global IDTariff
                IDTariff=(col[3],col[4])
                CHECK2=True
                print(CHECK1,CHECK2)
        if CHECK1==False or CHECK2==False:
            print("Try again")
    print("Success")

print("WELCOME")
while True:
    q = input('To enter the program, write AUTH. If you are a new user, write NEW. If you wish to stop the programm, write EXIT: ').upper()
    if q=="AUTH":
        account_auth()
        break
    elif q=="NEW":
        account_new()
        account_auth()
        break

if account_type==ClientsSheet:
    print('- Menu -\n'
          'Please select the menu number to work with the program\n'
          'My Tariff - 1\n'
          'My balance - 2\n'
          'Subscribe to Tariff - 3\n'
          'Exit the program - 0\n')
    print(IDTariff)
    option = int(input('Select an option: '))
    user_menu(option,IDTariff)

elif account_type==EmployeesSheet:
    print('- Employee menu -\n'
          'Please select the menu number to work with the program\n'
          'List of clients - 1\n'
          'Search - 2\n'
          'Customer history - 3\n'
          'Tariffs - 4\n'
          'Registration - 5\n'
          'Issuing tariffs - 6\n'
          'Exit the pr  ogram - 0\n')
    option = int(input('Select an option: '))
    user_menu(option)