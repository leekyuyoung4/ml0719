# 입력과 출력
# 2단 프로그램을 만단다.

# 함수이름은 gugudan
# 입력받는 값은 :2
# 출력은 2단 :  2 4 6 8 10 
# 결과는 어떤형태로 저장? : 연속된 데이터형태... 리스트

# result = gugudan(2)

def gugudan(n):
    return [ n*i for i in range(1,10)]