# 오늘 배운 내용 정리
# 상속, 모듈.

# 파이썬에서 상속은 특별한 추가코딩없이 바로 부모의 기능을 다 사용가능하고 자식클래스내부에서 부모는 self로 접근한다(생성자는 super()로 접근한다)
# 주의사항
# 자식이 생성자를 따로 안만들면 부모의 생성자를 기본적으로 호출
# 하지만 필요에 의해서 자식이 생성자를 만들면 자동으로 호출 안한다. =>super().__init__()

class A:    
    clsV = 'ca'
    def __init__(self,insVA='ia'):
        self.insVA = insVA
    def methodA(self):
        print("class A method")        

class B(A):
    clsV = 'cb'
    # def __init__(self,insVB='ib'):
    #     # super().__init__()
    #     self.insVB = insVB
    def methodB(self):
        print("class B method")   
    def myMethod(self):
        print(self.insVA)
        
b = B()
b.methodA()
b.methodB()  
b.myMethod() 
print(b.insVA)
# print(b.insVB)
        