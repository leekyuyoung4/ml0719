# 클래스
# 그 변수를 이용하는 맴버 함수를 갖게하고
# 생성자를 통해 맴버변수를 초기화

# 객체 생성해서 사용해 보기
# 그 객체가 하나가아니라 여러개 나올수도 있으니
# 그 객체를 보관하는 자료구조를
# 리스트로 저장해보고
# 투플로 저장해 보고
# set으로 만들어보고
# dictionary 형태로로 만들어보세요

class Temp:
    def __init__(self,num1=0,num2=0):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2

a = Temp()
b = Temp(1,10)
c = Temp()

list_a = [a,b,c]
tuple_a = (a,b,c)
set_a = (a,b,c)
dic_a = { 1 : a, 2:b, 3:c }

for i in list_a:
    print(f"list_a : {i.add()}")

for i in tuple_a:
    print(f"tuple_a : {i.add()}")

# dictionary 출력
print(f"dic_a key :1 value of add() : { dic_a.get(1).add()}")
# key값만 리스트형태로 받아서 for문을 이용해서 출력
for key in dic_a.keys():
    print(f"dic_a key :{key} value of add() : { dic_a.get(key).add()}")
# key value형태로 받아서 출력
# items()  튜플형태로 (key,value)
for key,value in  dic_a.items():
    print(f"key:{key} value:{value.add()}")