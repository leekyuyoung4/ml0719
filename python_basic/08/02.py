# 4칙연산 클래스에서 
# 1. 내부변수를 생성하는 메소드를 만든다 set0000
# 2. 필요한 메소드를 만든다

class FourClass:
    def setData(self, num1, num2):
        self.num1 = num1
        self.num2 = num2        
    def add(self):
        return self.num1 + self.num2
    def sub(self):
        return self.num1 - self.num2 
    def mul(self):
         return self.num1 * self.num2
    def div(self):
        if(self.num2 == 0):
            print("0으로 나눌수 없습니다.")        
        else:
            return self.num1 / self.num2

# 객체를 생성해서 4 2에 대한 4칙연산을 수행하고 결과를 출력    
# a 객체생성
a = FourClass()
a.setData(4,2)
result = a.add()  # AttributeError: 'FourClass' object has no attribute 'num1'
print(result)
a.num2 = 0
result = a.div()
print(result)

# 변수를 선언할때 값을 할당 안하고 생성하고 싶을때
temp = None # 타 언어에서는 null

