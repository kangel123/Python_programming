import random

winner = ""
# 공수 정하기(가위, 바위, 보)
while 1:
    user_choice = int(input("가위, 바위, 보 중 하나를 선택하시오(가위:1, 바위:2, 보:3) : "))
    computer_choice = random.randint(1, 3)
    result = user_choice - computer_choice
    print("사용자는 ", user_choice, "컴퓨터는 ", computer_choice)
    if result == 1 or result == -2:  # 사용자가 이겼을 때
        winner = "user"
        print("공격")
        break
    elif result == -1 or result == 2:  # 컴퓨터가 이겼을 때
        winner = "computer"
        print("수비")
        break
    else:  # 비겼을 때
        continue

# 묵찌빠
while 1:
    user_choice = int(input("가위, 바위, 보 중 하나를 선택하시오(가위:1, 바위:2, 보:3) : "))
    computer_choice = random.randint(1, 3)
    result = user_choice - computer_choice
    print("사용자는 ", user_choice, "컴퓨터는 ", computer_choice)

    if result == 1 or result == -2:
        winner = "user"
        print("공격")
    elif result == -1 or result == 2:
        winner = "computer"
        print("수비")
    else:  # 비겼을 때
        break

if winner == "user":
    print("승리")
else:
    print("패배")
