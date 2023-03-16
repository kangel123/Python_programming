print("\n3장 연습문제 3번")
n = int(input("정수를 입력해주세요 : "))
sum = 0
while n > 0:
    sum += n % 10
    n //= 10
print("자리수의 합 : ", sum)
