#   Pandas project          : Passport seva Analysis
#   Data Taken from         : Data.gov.in
#   Developed by            : XYZ
#   Roll No                 : 123434
#   session                 : 2022-23


#   function name           : clear()
#   purpose                 : clear output screen
def clear():
    for x in range(35):
        print()


#   function name           : DataFrame_creation_menu()
#   purpose                 : Create DataFrame from different type of data
def dataFrame_creation_menu():
    pass


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


# calling of main_menu function
main_menu()
