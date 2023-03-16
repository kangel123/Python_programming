items = {'커피음료': 7, '펜': 3, '종이컵': 2, '우유': 1, '콜라': 4, '책': 5}

while 1:
    print(items)
    item = input("물건의 이름을 입력하시오(종료:-1) : ")

    if item == "-1":
        break
    if item in items.keys():
        print("현재 재고는", items[item], "개 입니다.")
        c = int(input("1:수량 증가, 2:수량 감소 : "))
        n = int(input("수량의 개수를 입력해 주세요 : "))

        if c == 1:
            items[item] += n
        else:
            if items[item]-n > 0:
                items[item] -= n
            else:
                print("재고가 부족합니다.")


    else:
        print("물건의 이름을 다시 입력 해주세요.")

print("프로그램이 종료되었습니다.")
