# https://api.thedogapi.com/v1/breeds

import requests, json
# 1. Get a list of dog breeds from this API
r = requests.get('https://api.thedogapi.com/v1/breeds')
r = r.json()
# 2. Print each breed and its associated lifespan
# poodle -- 5 - 8 years
d = {}
for i in r:
    name = i['name']
    life_span = i['life_span']
    # b = name + ', ' + life_span
    if life_span in d:
        # add value to exisiting key
        d[life_span].append(name)
    else:
        # new entry
        d[life_span] = [name]

# print(d)

# 3. Group the breeds by lifespan
for pair in d:
    print(pair + ':')
    for i in d[pair]:
        print(i)
        print()

    # 5 - 8 years:
    # American Bulldog
    # poodle
    # Lab