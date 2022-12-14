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
    print('Add New Item Screen')
    print('-'*80)
    # recieve new item details from the keyboard
    item_no  = input('Enter Item No :')
    item_name = input('Enter Item Name :')
    item_price = input('Enter Item Price : ')

    # form sql from the given data
    sql = "insert into items values({},'{}',{})".format(item_no,item_name,item_price)
    #print(sql)

    # execute sql and save the changes
    cursor.execute(sql)
    conn.commit()
    
    print('\n\n\nNew Item Added Successfully')
    wait=input('\n\nPress any key to continue.....')


#   function name           : delRecord
#   purpose                 : To delete a food item from food table
def delRecord():
    clear()
    print('Delete Item Screen')
    print('-'*80)
    # recieve item No fom the keyboard
    item_no  = input('Enter Item No :')

    #form sql 
    sql = 'delete from items where no={}'.format(item_no)
    #print(sql)

    cursor.execute(sql)
    conn.commit()

    print('\n\n\nItem Deleted Successfully')
    wait=input('\n\nPress any key to continue.....')



#   function name           : updateRecord
#   purpose                 : To update food item's details in food table
def updateRecord():
    clear()
    print('Update Item Screen')
    print('-'*80)
    # recieve item No fom the keyboard
    item_no  = input('Enter Item No :')
    item_name = input('Enter New Item Name :')
    item_price = input('Enter New Price :')

    #form sql
    sql ="update items SET name='{}', price ={} where no ={}".format(item_name,item_price,item_no)
    #print(sql)

    cursor.execute(sql)
    conn.commit()

    print('\n\n\nItem Updated Successfully')
    wait=input('\n\nPress any key to continue.....')

#   function            : searchRecord()
#   purpose             : search food item from item table
def searchRecord():
    clear()
    print('Search Screen')
    print('-'*80)
    keyword = input('Enter Item Name :')

    sql = "select * from items where name like '%{}%'".format(keyword)
    #print(sql)
    cursor.execute(sql)
    results = cursor.fetchall()
    clear()
    print('Search Results for keyword :{}'.format(keyword))
    print('-'*80)
    for row in results:
        print(row)
    
    conn.close()
    wait=input('\n\nPress any key to continue.....')


#   function name           : billing()
#   purpose                 : to generate food bill
def billing():
    clear()
    print('Billing screen')
    print('-'*80)
    FoodItems =[]

    # find out food items from items table
    # and add into FoodItems lists
    while True :
        item=[]
        item_no = input('Enter Item No :')
        if item_no=='0':
            break

        sql = "select * from items where no ={}".format(item_no)
        cursor.execute(sql)
        result=cursor.fetchone()
        if result !=None:
            if len(result)<=0:
                print('Item No does not exists.......')
                wait= input('\n\nress any key.....')
            else:
                qty = int(input('Enter Quantity :'))
                item =[item_no,result[1],result[2],qty]
                FoodItems.append(item)
        
    #print(FoodItems)
    clear()
    print('ABC Restaurant'.center(80,'*'))
    print('-'*80)
    print('Item No          Item Name        Price      Qty      Amount')
    print('-'*80)
    total_amount=0
    for row in FoodItems:
        amount = row[2]*row[3]
        total_amount +=amount
        print(row[0],row[1],row[2],row[3],amount)
    print('-'*80)
    print('Payable amount',total_amount)

    wait= input('\n\nPress any key to continue.....')




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
            #wait = input('Enter any key ........')
        if choice==2:
            delRecord()
            #wait = input('Enter any key ........')
        if choice==3:
            updateRecord()
            #wait = input('Enter any key ........')
        if choice==4:
            searchRecord()
            #wait = input('Enter any key ........')
        if choice==5:
            billing()
            wait = input('Enter any key ........')
        if choice==6:
            break


main_menu()