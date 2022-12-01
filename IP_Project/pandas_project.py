#   Pandas project          : Passport seva Analysis
#   Data Taken from         : Data.gov.in
#   Developed by            : XYZ
#   Roll No                 : 123434
#   session                 : 2022-23

import pandas as pd
import time

#   function name       : intro()
#   purpose             : Display introduction of your project on the screen


def intro():
    msg = "This is me rakesh and this is my small project made using python\
        pandas and python for the partial fulfillment of project work in Information\
        technology subject for the session 2022-23. \
        This project was made by : YourName and Your PartnerName\
        under the guidance of Mr. Rakesh Kumar"
    for x in msg:
        print(x, end='')
        # time.sleep(0.0001)

    wait = input('\n\n\nPress any key to continue.......')


#   function name           : thanks()
#   purpose                 : display thanks message on the screen
def thanks():
    msg = "Thank you very much for evaluating our project\
        hope you will like it.\
        - Your Name\
        - Your Partner Name"
    for x in msg:
        print(x, end='')
    wait = input('\n\n\nPress any key to continue......')

#   function name           : clear()
#   purpose                 : clear output screen


def clear():
    for x in range(35):
        print()


#   function name           : DataFrame_creation_menu()
#   purpose                 : Create DataFrame from different type of data
def dataFrame_creation_menu():
    while True:
        clear()
        print('DATAFRAME CREATION MENU '.center(80, ' '))
        print('-'*80)
        print('\n1.   Using List of List')
        print('\n2.   Using Tuples')
        print('\n3.   Using Dictionary of List')
        print('\n4.   Using List of Dictionary')
        print('\n5.   Using DataFrame Series')
        print('\n6.   Import Data From CSV File')
        print('\n7.   Exit')
        choice = input('\n\nEnter your choice (1..7):')
        if choice == '1':
            print('you selected list of list ')
            data = [[12, 34, 45, 67, 67], [23, 45, 56, 67, 78], [34, 56, 67, 78, 45],
                    [34, 456, 67, 78, 89]]
            df = pd.DataFrame(data)
            print(df)
            wait = input('\n\nPress any key to continue....')
        if choice == '2':
            print('you have selected dataFrame using tuple')
            data = (
                (12, 34, 45, 67, 67),
                (23, 45, 56, 67, 78),
                (34, 56, 67, 78, 45),
                (34, 456, 67, 78, 89)
            )
            df = pd.DataFrame(data)
            print(df)
            wait = input('Press any key to continue....')
        if choice == '3':
            print('Dictionary of list')
            data = {
                'admno': [101, 102, 103, 104, 105, 106],
                'name': ['khushi', 'prashant', 'mukul', 'oieshik', 'vignesh', 'mahir'],
                'ip': [34, 56, 78, 89, 89, 88],
                'bs': [67, 89, 4, 78, 34, 98],
                'eco': [56, 78, 45, 89, 89, 23]
            }
            df = pd.DataFrame(data)
            print(df)
            wait = input('\n\n\nPress any key to continue....')
        if choice == '4':
            print('DataFrame Creation using List of dictionary  ')
            data = [
                {'admno': 102, 'name': 'rakesh', 'ip': 90, 'eco': 98, 'bs': 89},
                {'admno': 103, 'name': 'jai', 'ip': 89, 'eco': 67, 'bs': 89},
                {'admno': 104, 'name': 'vikas', 'ip': 67, 'eco': 67, 'bs': 67},
                {'admno': 105, 'name': 'ramesh', 'ip': 78, 'eco': 67, 'bs': 89},
                {'admno': 106, 'name': 'udit', 'ip': 74, 'eco': 56, 'bs': 89}
            ]
            df = pd.DataFrame(data)
            print(df)
            wait = input('Press any key to continue....')
        if choice == '5':
            print('DataFrame using Pandas Series ')
            s1 = pd.Series([45, 56, 78, 345, 68, 89, 90])
            print(s1)
            df = pd.DataFrame(s1)
            print(df)
            # data_visualization_menu()
            wait = input('\n\n\nPress any key to continue....')
        if choice == '6':
            print('Data Visualization ')
            # data_visualization_menu()
            wait = input('Press any key to continue....')
        if choice == '7':
            break

#   function name           : DataFrame_analysis_menu()
#   purpose                 : Display dataFrame Analysis menu on the screen


def dataframe_analysis_menu():
    while True:
        clear()
        print('DATAFRAME ANALYSIS MENU '.center(80, ' '))
        print('-'*80)
        print('\n1.   Display whole DataFrame')
        print('\n2.   Display All Columns')
        print('\n3.   Display Last 10 Rows')
        print('\n4.   Display Top 10 Rows')
        print('\n5.   Add a New Column')
        print('\n6.   Change the Name of Column')
        print('\n7.   Delete a Column')
        print('\n8.   Add A New Row')
        print('\n9.   Delete a Row')
        print('\n10.  Filter Rows and Columns')
        print('\n11.  Exit')
        choice = input('\n\nEnter your choice (1..11):')
        if choice == '1':
            print('you selected dataframe creation menu')
            # dataframe_creation_menu()
            wait = input('Press any key to continue....')
        if choice == '2':
            print('you have selected dataframe analysis menu')
            # dataframe_analysis_menu()
            wait = input('Press any key to continue....')
        if choice == '3':
            print('Data Visualization ')
            # data_visualization_menu()
            wait = input('Press any key to continue....')
        if choice == '4':
            print('Data Visualization ')
            # data_visualization_menu()
            wait = input('Press any key to continue....')
        if choice == '5':
            print('Data Visualization ')
            # data_visualization_menu()
            wait = input('Press any key to continue....')
        if choice == '6':
            print('Data Visualization ')
            # data_visualization_menu()
            wait = input('Press any key to continue....')
        if choice == '7':
            print('Data Visualization ')
            # data_visualization_menu()
            wait = input('Press any key to continue....')
        if choice == '8':
            print('Data Visualization ')
            # data_visualization_menu()
            wait = input('Press any key to continue....')
        if choice == '9':
            print('Data Visualization ')
            # data_visualization_menu()
            wait = input('Press any key to continue....')
        if choice == '10':
            print('Data Visualization ')
            # data_visualization_menu()
            wait = input('Press any key to continue....')
        if choice == '11':
            break


#   function name           : data_visual_menu()
#   purpose                 : display data visualization menu
def data_visual_menu():
    while True:
        clear()
        print('DATA VISUALIZATION MENU '.center(80, ' '))
        print('-'*80)
        print('\n1.   LINE CHART ')
        print('\n2.   BAR CHART')
        print('\n3.   HISTOGRAM')
        print('\n4.   Exit')
        choice = input('\n\nEnter your choice (1..4):')
        if choice == '1':
            print('you selected dataframe creation menu')
            # dataframe_creation_menu()
            wait = input('Press any key to continue....')
        if choice == '2':
            print('you have selected dataframe analysis menu')
            # dataframe_analysis_menu()
            wait = input('Press any key to continue....')
        if choice == '3':
            print('Data Visualization ')
            # data_visualization_menu()
            wait = input('Press any key to continue....')
        if choice == '4':
            break


#   function name           : main_menu
#   purpose                 : Generate main menu for Project
def main_menu():
    while True:
        clear()
        print('M A I N    M E N U'.center(80, ' '))
        print('-'*80)
        print('\n1.   DataFrame Creation')
        print('\n2.   DataFrame Analysis')
        print('\n3.   Visualization')
        print('\n4.   Exit')
        choice = input('\n\nEnter your choice (1..4):')
        if choice == '1':
            #print('you selected dataframe creation menu')
            dataFrame_creation_menu()
            #wait = input('Press any key to continue....')
        if choice == '2':
            #print('you have selected dataframe analysis menu')
            dataframe_analysis_menu()
            #wait = input('Press any key to continue....')
        if choice == '3':
            #print('Data Visualization ')
            data_visual_menu()
            #wait = input('Press any key to continue....')
        if choice == '4':
            break


# calling of main_menu function
intro()
main_menu()
thanks()
