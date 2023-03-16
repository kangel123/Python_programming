import random

user = 0
computer = 0
n = 5

while n > 0 and user < 3 and computer < 3:  # 5판 중 3판 이길 때까지
    user_choice = int(input("가위, 바위, 보 중 하나를 선택하시오(가위:1, 바위:2, 보:3) : "))
    computer_choice = random.randint(1, 3)
    result = user_choice - computer_choice

    print("사용자는 ", user_choice, "컴퓨터는 ", computer_choice)
    if result == 1 or result == -2:         # 사용자가 이겼을 때
        user += 1
        n -= 1
    elif result == -1 or result == 2:       # 컴퓨터가 이겼을 때
        computer += 1
        n -= 1
    else:                                   # 비겼을 때
        continue

if user > computer:
    print("사용자 승리!")
elif user < computer:
    print("컴퓨터 승리!")
else:
    print("무승부")
