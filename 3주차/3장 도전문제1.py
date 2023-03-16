americano_price = 2000
cafelatte_price = 3000
capucino_price = 3500

americano = int(input("아메리카노 판매 개수 : "))
cafelatte = int(input("카페라떼 판매 개수 : "))
capucino = int(input("카푸치노 판매 개수 : "))

sales = americano*americano_price + cafelatte*cafelatte_price + capucino*capucino_price
print("총 매출은, ", sales, "입니다.")
if sales < 100000:
    print("현재 적자입니다.")
else:
    print("현재 흑자입니다.")