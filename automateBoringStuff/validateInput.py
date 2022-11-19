while True:
    print('Enter your age: ')
    age = input()
    if age.isdecimal():
        break
    else:
        print('Please enter a number for age, chief.')

while True:
    print('Select a new password (letters and numbers only)')
    password = input()
    if password.isalnum():
        break
    else:
        print('Passwords can only contain letters and numbers, son.')