import time

# '+'를 사용한 경우
print("case : +")
now = time.time()
thisYear = int(1970 + now//(365*24*3600))

print("올해는 " + str(thisYear) + "입니다.")
age = int(input("몇 살이신지요? "))
print("2050년에는 " + str(age + 2050 - thisYear) + "살 이시군요.")

# ','를 사용한 경우
print("\ncase : ,")
now = time.time()
thisYear = int(1970 + now//(365*24*3600))

print("올해는 ", thisYear, "입니다.")
age = int(input("몇 살이신지요? "))
print("2050년에는 ", age + 2050 - thisYear, "살 이시군요.")
