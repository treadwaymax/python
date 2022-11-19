import random
def getAnswer(answerNum):
    if answerNum == 1:
        return 'it is certain'
    if answerNum == 2:
        return 'it is decidely so'
    if answerNum == 3:
        return 'You know it, baby'
    if answerNum == 4:
        return 'Reply hazy. Try again.'
    if answerNum == 5:
        return 'Ask again later'
    if answerNum == 6:
        return 'Ask your mom when she gets home'
    if answerNum == 7:
        return 'My reply is no'
    if answerNum == 8:
        return 'Outlook is not good'
    if answerNum == 9:
        return 'Super doubtful'
print(getAnswer(random.randint(1, 9)))