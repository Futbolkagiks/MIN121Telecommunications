from functionsForAuth import *
from menu import *
from typing import Tuple
from openpyxl import load_workbook
import openpyxl
workbook=load_workbook(filename="Users.xlsx")
EmployeesSheet=workbook["Employees"]
ClientsSheet=workbook["Clients"]
Tariffs=load_workbook(filename="Tariffs.xlsx")


print("WELCOME")
q = input('To enter the program, write AUTH. If you are a new user, write NEW. If you wish to stop the programm, write EXIT: ')
if q=="AUTH":
    account_auth()
elif q=="NEW":
    account_new()

if account_type==ClientsSheet:
    print('- Menu -\n'
          'Please select the menu number to work with the program\n'
          'My Tariff - 1\n'
          'My balance - 2\n'
          'Subscribe to Tariff - 3\n'
          'Exit the program - 0\n')
    option = int(input('Select an option: '))
    user_menu(option)

elif account_type==EmployeesSheet:
    print('- Employee menu -\n'
          'Please select the menu number to work with the program\n'
          'List of clients - 1\n'
          'Search - 2\n'
          'Customer history - 3\n'
          'Tariffs - 4\n'
          'Registration - 5\n'
          'Issuing tariffs - 6\n'
          'Exit the program - 0\n')