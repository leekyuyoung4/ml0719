# instance value 객체 변수
class Dumy:
    classNumber = 100
    def __init__(self,number):
        self.number = number  # 객체변수(독립적인 메모리)
        
    

# 객체 3개 생성
a = Dumy(10) 
b = Dumy(20)   
c = Dumy(30)        
print(f"a of number:{a.number} b of number:{b.number} c of number:{c.number}")
# a of number:10 b of number:20 c of number:30

# a b c 객체의 classNumber는 클래스 변수(동일메모리)
print(f"a of clsNumber:{a.classNumber} b of clsNumber:{b.classNumber} c of clsNumber:{c.classNumber}")

# 객체를 통해서 클래스변수에 접근해서 값을 할당하면
# slelf.클래스변수 = 값
# 클래스변수와 동일한 이름의 인스턴스 변수를 생성
a.classNumber = 1000
print(f"a of clsNumber:{a.classNumber} b of clsNumber:{b.classNumber} c of clsNumber:{c.classNumber}")
# a of clsNumber:1000 b of clsNumber:100 c of clsNumber:100

# 객체를 통해서 클래스에 미리 생성하지 않는 변수를  생성할수 있다.
a.hello = "안녕하세요"
print(a.hello)

# 파이썬에서는 클래스변수는 특별히 목적이 있으니
# 해당 클래스변수로 인스턴스변수를 생성하지 않는다  