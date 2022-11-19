birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (enter nothing to exit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(f'{birthdays[name]} is the birthday of {name}')
    else:
        print(f'I ain\'t got a birthday for {name}')
        print('What\'s their birthday?')
        bday = input()
        if bday == '':
            print('No birthday entered. Please enter a real bithday')
            bday = input()
        birthdays[name] = bday
        print('Birthday information updated.')