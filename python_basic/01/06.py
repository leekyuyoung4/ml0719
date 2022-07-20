# bmi 계산
# bmi = 체중(kg) / ( 키(m) * 키(m))
# 키보드로 숫자를 입려하면... 정수가 아니다..... 문자형태의 숫자  값에다가
# int(문자형 숫자)  float(문자형 실수)

# 체중을 입력하세요
# 키를 입력하세요
# bmi는 000 입니다.

weight =  int(input("몸무게를 입력하세요 : "))
height = int(input("키를 입력하세요(cm) : "))   # 165cm  -> 1.65m

# height 는 m가 기본단위 - cm->m
height = height / 100

# bmi 계산 
bmi = weight / (height**2)

# 리포트
report = f"키:{height}cm, 몸무게:{weight}kg 의 BMI : {round(bmi,2)}"
print(report)