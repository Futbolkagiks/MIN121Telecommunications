from functionsForReg import *
from typing import Tuple
from openpyxl import load_workbook
import openpyxl
from colorama import init, Fore, Back, Style
workbook=load_workbook(filename="Users.xlsx")
EmployeesSheet=workbook["Employees"]
ClientsSheet=workbook["Clients"]
VVX=load_workbook(filename="Tariffs.xlsx")
Tariffs=VVX["Tariffs"]

def showTariffs():
    sheet = Tariffs['Sheet1']
    for row in sheet.iter_rows():
        for cell in row:
            print(Fore.CYAN, Style.BRIGHT + f' {cell.value:7}', end=' ')
        print()

def clients():
    for row in ClientsSheet.iter_rows(max_col=3):
        for cell in row:
            print(Fore.LIGHTGREEN_EX, Style.BRIGHT + f' {cell.value}', end=' ')
        print()

def user_menu(option,IDTariff):
    while True:
        if option == 1:
            for col in Tariffs.iter_rows(min_col=1,max_col=3,min_row=2,values_only=True):
                if col[0]==IDTariff[0]:
                    ActiveT=col[1]
            for col in Tariffs.iter_rows(min_col=1,max_col=3,min_row=2,values_only=True):
                if col[0]==IDTariff[1]:
                    PreviousT=col[1]
            print("Your active Tariff is {} \n".format(ActiveT))
            print("Your previous Tariff was {}".format(PreviousT))
            break
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
