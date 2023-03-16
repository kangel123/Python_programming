sec = int(input("초를 입력하세요 : "))
min = sec // 60
sec %= 60
print(min, "분 ", sec, "초")
