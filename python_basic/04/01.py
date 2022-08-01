# bmi = 몸무게(kg)/(키(m)*키(m))
# 저체중 : ~ 18.4
# 정상 : 18.5 ~ 22.9 
# 과체중 : 23.0 ~ 24.9
# 비만 : 25.0 ~

# input("키를 입력하세요 :")
# input("몸무게를 입력하세요 :")

# bmi지수는 20.5 이고 정상 입니다.

heigth = int(input("키를 입력하세요(cm) :"))
weight = int(input("몸무게를 입력하세요(kg) :"))

# 단위변경  cm -> m  /100

# heigth = heigth/100;
heigth /= 100
bmi = weight/(heigth**2)

result = "";
if bmi >= 25.0:
    result = '비만'
elif bmi >= 23.0:
    result = '과체중'
elif bmi >= 18.5:
    result = '정상'
else:
    result = '저체중'
    
print(f"bmi지수는 {round(bmi,1)}  {result} 입니다.")    
    





