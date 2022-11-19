import random
messages = ['It is certain',
            'It is decidely so',
            'Yes, defintely',
            'Reply hazy try again',
            'Ask again later, bruh'
            'Concentrate, and ask again, homie',
            'My reply is no',
            'Outlook, not so good dude',
            'Very, very doubtful, son'
            ]
print('Welcome to magic 8 ballz.')
print('Enter your question below to receive an answer.')
sheeple = input()
print(messages[random.randint(0, len(messages)-1)])