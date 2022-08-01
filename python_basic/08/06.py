# 메소드 이해하기
class MyClass:
    
    def sayHello(self):
        print("안녕하세요")
    def sayBye(self, name):
        print(f"{name}! 다음에 보자")

a = MyClass()
a.sayHello()
a.sayBye("철수") 