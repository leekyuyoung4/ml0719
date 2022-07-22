from curses import A_ALTCHARSET
from re import A


jumsu = int(input("점수를 입력하세요(0 ~ 100 : )" ) )
hakjum = 'F'  # 초기화

if jumsu >= 90:
    hakjum = 'A'    
elif jumsu >= 80:    # 89 87 86 85 .... 80
    hakjum = 'B'
elif jumsu >=70 :               # 79 ~~~~~~~ 70
    hakjum = 'C'
elif jumsu >=60:        # 69 ~ 60
    hakjum = 'D'
else:
    hakjum = 'F'    
    
    

print(f"점수는 {jumsu}이고 학점은 {hakjum} 입니다. ")

