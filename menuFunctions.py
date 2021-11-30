from os import read
from functionsForReg import *
from typing import Tuple
from openpyxl import load_workbook
import pandas as pd
from colorama import init, Fore, Back, Style
import csv

appl = pd.read_csv('Applications.csv', delimiter=',')
workbook=load_workbook(filename="Users.xlsx")
EmployeesSheet=workbook["Employees"]
ClientsSheet=workbook["Clients"]
VVX=load_workbook(filename="Tariffs.xlsx")
Tariffs=VVX["Tariffs"]

def showTariffs():
    for row in Tariffs.iter_rows(values_only=True):
        print(Fore.CYAN, Style.BRIGHT + f' {row}', end=' \n')
    return

def showMyTariff(details):
    while True:
        for col in Tariffs.iter_rows(min_col=1,max_col=3,min_row=2,values_only=True):
            if col[0]==details[5]:
                ActiveT=col[1]
        for col in Tariffs.iter_rows(min_col=1,max_col=3,min_row=2,values_only=True):
            if col[0]==details[6]:
                PreviousT=col[1]
        print(f"Your active Tariff is {ActiveT}")
        print(f"Your previous Tariff was {PreviousT}")
        return

def users_list(account_type):
    for col in account_type.iter_rows(values_only=True):
        info=[col[0],col[1],col[2],col[4]]
        print(Fore.LIGHTGREEN_EX, Style.BRIGHT + f' {info}', end=' \n')
    return

def searchClient():
    found=False
    name=str(input("Please input who you want to search: "))
    while True:
        for col in ClientsSheet.iter_rows(min_row=2,values_only=True):
            if (name.upper() in col[1].upper())==True:
                found=True
                print(col[0],col[1],col[2],col[4])
        if found==False:
            print("Your input was wrong. Try again")
            continue
        elif found==True:
            break
    return

def detailsClient():
    idClient=int(input("Please enter ID of the client whose history you wish to explore: "))
    for col in ClientsSheet.iter_rows(min_col=1,min_row=2,values_only=True):
        if col[0]==idClient:
            print(f"Client - {col[1]} /// Current tariff - {col[5]} /// Previous Tariff - {col[6]}")
    return

