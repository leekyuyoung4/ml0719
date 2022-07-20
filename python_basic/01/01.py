# 문자열 포멧팅 - 규칙적인 패턴을 가지는 문자열을 만들때
num1 = 10; num2 =  20

# 사칙연산 문자열..
print("%d + %d = %d" %( num1, num2, num1+num2) )
print("%d - %d = %d" %( num1, num2, num1-num2) )
print("%d * %d = %d" %( num1, num2, num1*num2) )
print("%d / %d = %d" %( num1, num2, num1/num2) )  # 0   # %d --> decimal
print("%d / %d = %f" %( num1, num2, num1/num2) )  # 0
# 0.5  %f는 소수점 6자리
print("%d / %d = %.2f" %( num1, num2, num1/num2 ) )  

print(num1/num2)  # 0.5

print( round(3.14157 ,2 ) )

# round(실수, 숫자)  해당 실수를 숫자만큼 원하는 자리수.. 반올림
from calendar import c
import math   # 필요한 라이브러리를 가져온다

# 내림
print(math.floor(3.14))
print(math.floor(3.99))

#올림
print(math.ceil(3.14))


# %d   정수
# %c   문자
# %s   문자열
# %f   실수
# %o   8진수
# %x   16진수

str = "이모델의 accuracy = %f  F-score = %f  F1 = %f 의 성능을 보입니다." %(95.8, 10, 10.5)
print(str)

print(f"이모델의 accuracy = {95.8}  F-score = {10}  F1 = {10.5} 의 성능을 보입니다.")