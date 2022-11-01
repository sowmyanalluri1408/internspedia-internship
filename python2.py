s='***WELCOME TO THE ADVENTURE***'
print(s.center(50))
print('\nType yes or no to move further in the game')
print('\nYou now have a stranger standing outside your house. He sees you and asks you for shelter.')
print('Will you provide shelter to him?')
a1=input('Yes or No? ')
if a1=='Yes':
    print('\nPolice arrived & asked whether the thief is inside.\nWhat will you answer?')
    a2=input('Yes or No? ')
    if a2=='No':
        print('\nGame Over')
    elif a2=='Yes':
        print('\nYOU WIN!!')
elif a1=='No':
    print('\nHe attacked you. Will you knock him down?')
    a3=input('Yes or No? ')
    if a3=='No':
        print('\nGame Over')
    elif a3=='Yes':
        print('\nYOU WIN!!')
else:
    print('\nERROR!')
