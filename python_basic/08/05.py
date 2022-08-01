class MyClass:
    hello = '안녕하세요'  # 전역변수 클래스내의 모든 곳에서
    def sayHello(self):
        variable1 = 10  # 지역변수 sayHello에서만 사용
        self.variable2 = 20 # 전역변수 클래스내의 모든 곳에서
        print(self.hello)

a = MyClass()
a.sayHello() 

b = MyClass()       
b.hello = '반갑습니다.'
b.sayHello()
