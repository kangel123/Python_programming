while 1:                        # 반복
    print("1.더하기")
    print("2.빼기")
    print("3.곱하기")
    print("4.나누기")
    print("5.종료")
    num = int(input("선택 : "))
    if num == 5:
        print("계산을 종료합니다.")
        break

    a = int(input("첫번째 숫자 : "))
    b = int(input("두번째 숫자 : "))
    if num == 1:
        result = a + b
        print("계산결과 : ", a, "+", b, "=", result)
    elif num == 2:
        result = a - b
        print("계산결과 : ", a, "-", b, "=", result)
    elif num == 3:
        result = a * b
        print("계산결과 : ", a, "*", b, "=", result)
    elif num == 4:
        try:
            result = a / b
            print("계산결과 : ", a, "/", b, "=", result)
        except ZeroDivisionError as e:
            print("계산오류 : 0으로 나눌 수 없다")
    else:
        print("선택오류 : 1,2,3,4 중에서 선택하시오")
    print("")
