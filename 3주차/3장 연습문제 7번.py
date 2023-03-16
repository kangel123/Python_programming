import time

print("\n3장 연습문제 7번")
minute = time.time()//60
hour = (minute//60) % 24
minute %= 60
print("현재 시간(영국 그리니치 시각): ", hour, "시", minute, "분")
