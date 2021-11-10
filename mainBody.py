from functionsForAuth import *
from typing import Tuple
from openpyxl import load_workbook
import openpyxl
workbook= load_workbook(filename="Users.xlsx")
EmployeesSheet=workbook["Employees"]
ClientsSheet=workbook["Clients"]

print("WELCOME")
q = input('To enter the program, write AUTH. If you are a new user, write NEW. If you wish to stop the programm, write EXIT: ')
if q=="AUTH":
    account_auth()
elif q=="NEW":
    account_new()

