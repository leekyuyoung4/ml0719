# 추가기능은 라이브러리를 import

print("%f" % 3.4152451)
print("%.2f" % 3.4152451)  # 기본적으로반올림을 함
print("%f" % 3.4152451)  # 기본적으로반올림을 함

# 3.4152451  소수2째 자리까지만 출력.... 반올림 없이
num1 = 3.4152451
num1 = num1 * 100
num1 = int(num1)
num1 = num1 / 100
print(num1)

