# 야구 게임
import random

randomNum = []
for i in range(4):
    a = random.randint(0, 9)
    while a in randomNum:
        a = random.randint(0, 9)
    randomNum.append(a)
count = 10
print('야구게임을 시작합니다.')
while count > 0:
    strike = 0
    ball = 0
    print('남은 기회:', count)
    num = input("숫자 4개를 이어서 입력하시오(중복X):")
    if int(num) < 123 or int(num) > 9876:
        print('잘못 입력했습니다')
    count -= 1
    numlist = list(map(int, list(num)))
    for i in range(len(randomNum)):
        for j in range(len(numlist)):
            if i == j and randomNum[i] == numlist[j]:
                strike += 1
            elif i != j and randomNum[i] == numlist[j]:
                ball += 1
    if strike == 4:
        print('성공')
        break
    elif count < 0:
        print(*randomNum, sep='')
        print('실패')
    print(strike, 'strike ', ball, 'ball')
