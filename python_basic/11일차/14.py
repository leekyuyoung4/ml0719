# 사용자로부터 입력을 받습니다.
# 그리고 입력받은 값을 출력합니다.
# 사용자가 입력한 값이 정수인지 실수 인지 문자인지 구별

# 위의 조건을 try~except를 이용해서 판단하고 출력할것

a = input('값을 입력하세요')
if a.isdigit():
    print("정수")
elif a.isalpha():
    print("문자")
else:     
    isFloat = True
    for i in a:    # 125.56
        if not(i.isdigit() or i == '.'):
           isFloat = False
           break        
    if isFloat:
        print("실수")
    else:
        print("정수 실수 문자가 아닌 형태의 입력입니다.")    
    
    