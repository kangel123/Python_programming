import random

x = random.randint(1, 100)
y = random.randint(1, 100)
computer_answer = x-y
user_answer = int(input(str(x) + "-" + str(y) + "="))

if computer_answer == user_answer:
    print("맞았습니다.")
else:
    print("틀렸습니다.")
