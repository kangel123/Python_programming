n = input('출력할 단을 입력하시오(예시:3, 4, 5) : ').replace(', ', '')
for i in n:
    for j in range(1, 10):
        print(i, ' * ', j, ' = ', int(i)*j)
