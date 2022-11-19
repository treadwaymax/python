def comma(lst):
    if len(lst) > 1:
        for i in lst[0:-1]:
            print(i + ', ', end='')
        print('and ' + lst[-1])
    else:
        print(i in list)

print('Sup nerd. Enter your list to witness the change bruh.')
lst = ['apples', 'bananas', 'tofu', 'cats']
comma(lst)
