from functionsForAuth import *
from typing import Tuple
from openpyxl import load_workbook
import openpyxl
workbook=load_workbook(filename="Users.xlsx")
EmployeesSheet=workbook["Employees"]
ClientsSheet=workbook["Clients"]
Tariffs=load_workbook(filename="Tariffs.xlsx")

##def showTariffs():

def user_menu(option):
    while True:
        if option == 1:
            for col in Tariffs["A"]:
                if col.value()==ClientsSheet["E{}".format(row)]:
                    ActiveT=Tariffs["B{}".format(col)]

            for col in Tariffs["A"]:
                if col.value()==ClientsSheet["F{}".format(row)]:
                    PreviousT=Tariffs["B{}".format(col)]

            print("Your active Tariff is {}".format(ActiveT))
            print("Your previous Tariff was {}".format(PreviousT))

        elif option == 2:
            balance=ClientsSheet["D{}".format(row)]
            print("Your balance is {}".format(balance))
        elif option == 3:
            showTariffs()
        elif option == 0:
            print('Thanks fo using our program. Goodbye!')
            break
        else:
            print('Invalid option')

#def worker_menu():
