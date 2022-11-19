#This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('I\'m thinking bout a number between 1 and 20.')

#Ask chump to guess six times.
for i in range(1, 7):
    print('Take a guess punk.')
    guess = int(input())
    if guess < secretNumber:
        print('Yo guess is too low, assbreath.')
    elif guess > secretNumber:
        print('Yo guess be too high, knucklenuts.')
    else:
        break # This is right number!
if guess == secretNumber:
    print('You got it in only ' + str(i) + ' guesses!')
    print('The number was ' + str(secretNumber))
else:
    print('You failed. The number I was thinking of was ' + str(secretNumber))
