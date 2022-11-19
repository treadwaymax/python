import random, sys
print('rock, paper, scissors')
#These variables will keep track of the number of wins, losses, and ties.
wins, losses, ties = 0, 0, 0
while True:
    print(f'Wins: {wins}, Losses: {losses}, Ties: {ties}')
    while True:
        print('Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit')
        print('Type one of r, p, s, or q')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quit program
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # break out of player input loop
    #Display input from player
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')
    #Display computer choice
    randomNum = random.randint(1, 3)
    if randomNum == 1:
        compMove = 'r'
        print('ROCK')
    elif randomNum == 2:
        compMove = 'p'
        print('PAPER')
    elif randomNum == 3:
        compMove = 's'
        print('SCISSORS')
    #Display and record win/loss/tie
    if playerMove == compMove:
        print('It\'s a mawfuggin tie')
        ties += 1
    elif playerMove == 'r' and compMove == 's':
        print('User wins.')
        wins += 1
    elif playerMove == 'p' and compMove == 'r':
        print('User wins.')
        wins += 1
    elif playerMove == 's' and compMove == 'p':
        print('User wins.')
        wins += 1
    elif playerMove == 'r' and compMove == 'p':
        print('Computer crushes you.')
        losses += 1
    elif playerMove == 'p' and compMove == 's':
        print('Computer crushes you.')
        losses += 1
    elif playerMove == 's' and compMove == 'r':
        print('Computer crushes you.')
        losses += 1