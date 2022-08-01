# inheritance : 물려받다
# 기존클래스를 물려받는다.
# 파이썬(프로그램) 상속은 기존 클래스의 기능 + 새로운기능 = 새로운 클래스
# 확장의 개념
# A 클래스를 상속받은 B 클래스
class A:
    def __init__(self):
        self.a = 100

class B(A): # B클래스는 A클래스를 상속(A클래의 모든 기능을 사용)
    pass

################
b = B()  # B클래스의 객체로 b를 선언함
print(b.a) # AttributeError: 'B' object has no attribute 'a'
