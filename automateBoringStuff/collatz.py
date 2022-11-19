# Collatz function
def collatz(num):
    try:
        if num % 2 == 0:
            num = (num // 2)
            print(num)
            return num
        elif num % 2 != 0:
            num = ((num * 3) + 1)
            print(num)
            return num
        else:
            return num
    except ValueError:
        print('You must enter an integer, bruh')
print('Enter a number for to witness the collatz mathematical phenomenon: ')
num = int(input())
while num != 1:
    num = collatz(num)