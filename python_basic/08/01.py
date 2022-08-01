# 학사관리
# 자료구조... 데이터를 어떻게 저장할 것인지
# 적절한 함수를 이용해서 해당 데이터를 처리

# 클래스 : 사용자가만든 새로운 자료구조및 타입..
# 변수 , 함수로 구성
# 설계도 라고도 하고 객체를 생성한다
# 객체는 dot연산자를 통해서 필요한 함수나 변수를 사용
# 클래스를 정의
class Cookie:
    pass

a =  Cookie()
b =  Cookie()

# 클래스에서 함수를 정의할때 첫번째 파라메터로 자신을 뜻하는
# self가 반드시 존재해야함
class FourCalc:    
    # 클래스 내부에 사용할 변수 만들기
    def setdata(self, first, second):
        self.first = first
        self.second = second
        

a = FourCalc()
print(type(a))  # <class '__main__.FourCalc'>
a.setdata(4,2)
print(a.first)   # 4
print(a.second)  # 2

a.first = 100
a.second = 200
print(a.first)  # 100
print(a.second) # 200

b = FourCalc()
b.setdata(1,2)
print(f"객체 b의 first = {b.first} second={b.second} 이고 객체 a의 first={a.first}, second={a.second}")

print(id(a.first))
print(id(b.first))

a = b  # 두객체가 같은 주소를가진다. a는 b의 주소를 가진다
a.first = 3.14
print(id(a.first))  # 둘다 동일한 주소
print(id(b.first)) # 둘다 동일한 주소

