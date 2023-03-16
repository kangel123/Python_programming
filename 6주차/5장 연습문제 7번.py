import random

Lotto = random.randint(0, 99)
lotto_number1 = Lotto // 10
lotto_number2 = Lotto % 10

choice = int(input("복권번호를 입력하시오: "))
choice_number1 = choice // 10
choice_number2 = choice % 10

print("당첨번호는 ", Lotto, "입니다.")

if Lotto == choice or (lotto_number1 == choice_number2 and lotto_number2 == choice_number1):
    print("상금은 100만원입니다.")
elif lotto_number1 == choice_number1 or lotto_number1 == choice_number2 or lotto_number2 == choice_number1 or lotto_number2 == choice_number2:
    print("상금은 50만원입니다.")
else:
    print("상금은 없습니다.")
