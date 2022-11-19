#! python3
import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    # Pick two random numbers:
    num1 = random.randint(0,16)
    num2 = random.randint(0,16)

    prompt = f'#{questionNumber}: {num1} x {num2} = '
    try:
        pyip.inputStr(prompt, allowRegexes=[f'{num1 * num2}$'], blockRegexes=[('.*', 'Incorrect')], timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of attempts!')
    else:
        print('Correct!')
        correctAnswers += 1
    time.sleep(1)
print(f'Score: {correctAnswers} / {numberOfQuestions}')