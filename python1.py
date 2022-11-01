import math
import random
lower=int(input('Enter the Lower Bound: '))
upper=int(input('Enter the Upper Bound: '))
random=random.randint(lower,upper)
chances=round(math.log(upper-lower+1,2))
print('\nYou only have',chances,'chances to guess the number')
c=0
while c<chances:
    n=int(input('\nGuess the number:'))
    if random==n:
        print('Congratulations! You guessed the number right!')
        break
    elif n>random:
        print('Try again! You guessed too high')
    elif n<random:
        print('Try again! You guessed too small')
    if n not in range(lower,upper+1):
        print('Enter a number between the lower and upper bounds only!!')
    c+=1
if c>=chances:
    print('\nThe number is ',random,'\nBetter Luck Next Time!')
