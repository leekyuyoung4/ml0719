# 에러.
# 예외.
# 많이 실수하는 에러의 유형
# 1. 배열의 인덱스가 넘어갈때
# 2. 0으로 나눌때
# 3. 입력을 받아서 정수로 변한할때. 문자를 정수로 변환..
# 4. 객체에서 객체가 생성되지 않았거나 없을때 그 맴버에 접근

class Dumy:
    def __init__(self,myValue=0):
        self.myValue = myValue

list_a = [10,20,30]
try:
    print(list_a[3]) # IndexError: list index out of range
except:
    print("예외가 발생했습니다.")

print(f"리스트의 총 합은 : {sum(list_a)}")


#print(10/0) # ZeroDivisionError: division by zero

# number = int("123a") # ValueError: invalid literal for int() with base 10: '123a'

# a =  Dumy()
# a = None
# a.myValue #A ttributeError: 'NoneType' object has no attribute 'myValue'

