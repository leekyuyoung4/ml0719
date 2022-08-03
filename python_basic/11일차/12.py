class Person:
    def __init__(self,name='',age=0):
        self.name = name
        self.age = age

persion = Person('홍길동',100)        
print(persion) # <__main__.Person object at 0x0000023BEFE57C40>

# 객체를만들고 그 객체를 출력하면
# 객체가 가지고 있는 모든 데이터 출력하자.
class Human:
    def __init__(self,name='',age=0):
        self.name = name
        self.age = age
    def __str__(self):
        return self.name+" " + str(self.age)
        
human = Human('홍길동',100)        
print(human)