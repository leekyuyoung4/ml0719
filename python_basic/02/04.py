# 입력한문자열이 문자열인지 숫자형태의 문자인지 구분해 주는 함수
number = input("숫자를입력하세요 : ")
# number는 문자열 
# 숫자로 변경하기전에 check
print( number.isdigit() )
print( number.isalpha() )
number = int(number) 