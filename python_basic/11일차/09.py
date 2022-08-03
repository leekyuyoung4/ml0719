# 예외의 응용
# 상속을 받는 자식이 반드시 부모가 가지고있는
# 메소드의 내용을 작성하게 강제하는 방법

class Animall:
    def __init__(self,name):
        self.name = name
    def bark(self):
        raise NotImplementedError

class Dog(Animall):
    def bark(self):
        print(f"{self.name}이 멍멍하고 짖습니다.")

class Cat(Animall):
    pass

# 바둑이 객체
dog = Dog("바둑이")
dog.bark()
# 나비 객체        

cat = Cat("나비")        
cat.bark()

# raise exception : 예외발생 기법을 부모 클래스에 적용하면
# 부모는 추상적으로(껍대기) 메소드를 만들고
# 자식클래스가 자신에 맞게 구현하도록 유도할수 있다