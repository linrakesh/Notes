# billing project by using python mysql project
# made by        : xyx
# session
# roll          :

import mysql.connector as mysql

#   function name           : clear
#   purpose                 : clear output screen


def clear():
    for x in range(35):
        print()


#   function name       : add_record()
#   purpose             : Add a new item in items table
def add_record():
    conn = mysql.connect(host='localhost', user='root',
                         password='', database='davfood')
    cursor = conn.cursor()
    clear()
    print('Add New Item Screen')
    print('-'*80)
    no = input('Enter Item No (PK):')
    name = input('Enter item Name :')
    price = input('Enter Item Price in INR :')
    sql = "insert into items values({},'{}',{})".format(no, name, price)
    # print(sql)
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('Item added successfully')


#   function name       : delete_record()
#   purpose             : delete an item from items table
def delete_record():
    conn = mysql.connect(host='localhost', user='root',
                         password='', database='davfood')
    cursor = conn.cursor()
    clear()
    print('Delete Item Screen')
    print('-'*80)
    no = input('Enter Item No (PK) to delete:')

    sql = "delete from  items where no ={}".format(no)
    # print(sql)
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('Item Deleted successfully')


#   function name       : modify_record()
#   purpose             : modify an item from items table
def modify_record():
    conn = mysql.connect(host='localhost', user='root',
                         password='', database='davfood')
    cursor = conn.cursor()
    clear()
    print('Modify Item Screen')
    print('-'*80)
    no = input('Enter Item No (PK) to modify:')
    name = input('Enter New Name :')
    price = input('Enter new Price :')
    sql = "update items set name ='{}', price ={} where no ={}".format(
        name, price, no)
    # print(sql)
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('Item Updated successfully')


# function name         :search_item
# purpose                : search an item based on its name
def search_item():
    conn = mysql.connect(host='localhost', user='root',
                         password='', database='davfood')
    cursor = conn.cursor()
    clear()
    print('Search Item Screen')
    print('-'*80)
    name = input('Enter Item Name:')
    sql = "select * from items where name like '%{}%'".format(name)
    # print(sql)
    cursor.execute(sql)
    results = cursor.fetchall()
    for result in results:
        print(result)
    conn.close()


#  function name            : search_price
#   purpose                 : search item between two price band
def search_price():
    conn = mysql.connect(host='localhost', user='root',
                         password='', database='davfood')
    cursor = conn.cursor()
    clear()
    print('Search Price wise Item Screen')
    print('-'*80)
    price1 = input('Enter first Price :')
    price2 = input('Enter second Price :')
    sql = "select * from items where price between {} and {}".format(
        price1, price2)
    # print(sql)
    cursor.execute(sql)
    results = cursor.fetchall()
    for result in results:
        print(result)

    conn.close()

#   function name           : search_menu
#   purpose                 : Generate search menu for billing system
def search_menu():
    while True:
        clear()
        print('Search Menu ')
        print('-'*80)
        print('\n1.   Search Item')
        print('\n2.   Price Wise Search')
        print('\n3.   Exit')
        choice = input('\n\nEnter your choice (1..3):')
        if choice == '1':
            print('you selected search item')
            search_item()
            wait = input('Press any key to continue....')
        if choice == '2':
            print('you have selected search price range')
            search_price()
            wait = input('Press any key to continue....')
        if choice == '3':
            break


#   function name   : billing
#   purpose         : Generate food bill for customer
def billing():
    conn = mysql.connect(host='localhost', user='root',
                         password='', database='davfood')
    cursor = conn.cursor()
    clear()
    print('Billing Screen')
    print('-'*80)
    items = []
    while True:
        no = input('Enter Item No :')
        if no == '0':
            break
        sql = 'select * from items where no ={}'.format(no)
        cursor.execute(sql)
        result = cursor.fetchone()
        if result == None:
            print('Item No does not exist.....')
        else:
            qty = int(input('Enter quantity :'))
            item = [result[0], result[1], result[2], qty]
            items.append(item)

    clear()
    print('XYZ Restaurant')
    print('-'*80)
    print('Food Bill')
    print('-'*80)
    bill = 0
    for item in items:
        print(item[0], item[1], item[2], item[3], item[2]*item[3])
        bill += item[2]*item[3]
    print('-'*80)
    print('Total Payable amount :', bill)
    print('-'*80)

    wait = input('\n\n\nPress any key to continue....')


def main_menu():
    while True:
        clear()
        print('M A I N    M E N U  ')
        print('\n1.   Add New Item')
        print('\n2.   Delete Item')
        print('\n3.   Modify item')
        print('\n4.   Search Item')
        print('\n5.   Billing')
        print('\n6.   Exit')
        choice = input('\n\nEnter your choice (1..6):')
        if choice == '1':
            #print('you selected add new item')
            add_record()
            wait = input('Press any key to continue....')
        if choice == '2':
            #print('you have selected delete item')
            delete_record()
            wait = input('Press any key to continue....')
        if choice == '3':
            #print('modify item')
            modify_record()
            wait = input('Press any key to continue....')
        if choice == '4':
            #print('search item ')
            search_menu()
            wait = input('Press any key to continue....')
        if choice == '5':
            # print('billing')
            billing()
            wait = input('Press any key to continue....')
        if choice == '6':
            break


main_menu()
