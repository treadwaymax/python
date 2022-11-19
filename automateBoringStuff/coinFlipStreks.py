import random, copy

numStreaks = 0
streak = 0
lst = []
for experimentNum in range(10000):
    #code that creates a list of 100 h/t flips
    for i in range(100):
        i = random.randint(0,1)
        if i == 0:
            lst.append('t')
        elif i == 1:
            lst.append('h')
# code that checks if thers a streak of 6 heads or tails in a row
for i in range(1, len(lst)):
    if lst[i] == lst[i-1]:
        streak += 1
    else:
        streak = 0
    if streak == 6:
        numStreaks += 1
print(f'Chance of streak: {(numStreaks / (100 * 10000)) * 100}%')


