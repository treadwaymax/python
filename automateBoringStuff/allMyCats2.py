catNames = []
while True:
    print('Enter the name of cat number ' + str(len(catNames)+1) + ' or enter "done" to stop.')
    name = input()
    if name == 'done':
        break
    catNames += [name]
print('The cat names are: ')
for name in catNames:
    print('     ' + name)
