# 상속을 받게 되면 부모의 생성자를 호출해서
# 객체를  생성한다.
# 1. 부모생성자 / 2. 자신의 생성자 / 3. 객체 생성
# 부모로부터 물려받은 기능이 해당 클래스에서
# 적합하지않을때 재 정의 한다 - override(overwrite) 라고 함

class Animal:
    def __init__(self,age,name):
        self.age = age
        self.name = name
        
    def bark(self):
        print("동물이 짖는소리")

class Dog(Animal):
    def bark(self):
        print("멍멍~~~")

class Cat(Animal):
    def __init__(self, age=0, name=''):
        # 자식에서 부모를 호출할때는 super()를 사용한다.
        super().__init__(age, name) 
    def bark(self):
        print("야용~~")
        
#########################
# 상속을 받으면 그 자식클래스는 객체가 돨때
# 부모의 생성자를 호출하고 그리고 자신의 생성자를 호출
# 해서 객체를 생성한다
dog = Dog(1,'바둑이')
cat = Cat()

dog.bark()
cat.bark()


