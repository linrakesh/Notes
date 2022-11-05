# Python project for food billing system for ABC Restaurant
# made by           : rakesh kumar
# session           : 2022-23
# Front-end         : Python
# Backend           : Mysql
# DataBase Name     : foodbilling
# table-name        : items
# User Name         : anu
# user Password     : pass1


import mysql.connector as mysql

#define two global variable
conn = mysql.connect(host='localhost',user='anu',password='pass1',database='foodbill')
cursor = conn.cursor()

#function           ":clear
#purpose            : clear output screen
def clear():
    for x in range(25):
        print()


#   function name           : addRecord
#   purpose                 : To add a new food item in food table
def addRecord():
    clear()
    print('Add function called')


#   function name           : delRecord
#   purpose                 : To delete a food item from food table
def delRecord():
    clear()
    print('delete vcalled')

#   function name           : updateRecord
#   purpose                 : To update food item's details in food table
def updateRecord():
    clear()
    print('updated invloked')



#   function            : searchRecord()
#   purpose             : search food item from item table
def searchRecord():
    clear()
    print('search function called')

#   function name           : billing()
#   purpose                 : to generate food bill
def billing():
    clear()
    print('billing function called')



def main_menu():
    while True:
        clear()
        print('Food Billing System'.center(80,'*'))
        print('\n1.   Add New Food Item')
        print('\n2.   Delete Food Item')
        print('\n3.   Update Food Item')
        print('\n4.   Search Food Item')
        print('\n5.   Billing')
        print('\n6.   Exit')
        choice= int(input('\n\nEnter your choice (1:6) : '))
        if choice==1:
            addRecord()
            wait = input('Enter any key ........')
        if choice==2:
            delRecord()
            wait = input('Enter any key ........')
        if choice==3:
            updateRecord()
            wait = input('Enter any key ........')
        if choice==4:
            searchRecord()
            wait = input('Enter any key ........')
        if choice==5:
            billing()
            wait = input('Enter any key ........')
        if choice==6:
            break


main_menu()