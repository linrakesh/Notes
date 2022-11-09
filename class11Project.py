while True:
    for x in range(45):
        print()
    print('     MAIN MENU  ')
    print('-'*80)
    print('\n1.   Stone Paper Scissor')
    print('\n2    Hangman')
    print('\n3.   tic Tac Toe')
    print('\n4.   Exit')
    choice = input('\n\nEnter your choice :')
    if choice =='1':
        print('You have selected Stone Paper Scissor')
        wait=input('\n\nPress any key to continue....')
    if choice=='2':
        print('You have selected Hangman')
        wait=input('\n\nPress any key to continue....')
    if choice=='3':
        print(' You have selected Tic Tac Toe')
        wait=input('\n\nPress any key to continue....')
    if choice =='4':
        break