# 클래스 만들기
# 변수정의하기 - 클래스내부에 직접 
#   변수명 = 적당한 값    
# or
#   함수를 통해 self.변수명 = 적당한 값
#   장점 : 생성자를 이용할수 있다.
#   생성자 : 객체생성시 자동호출 - 초기화
#       def __init__()  생성자라고 불리는 함수
#   __시작하는 함수나 변수는 내부에서 미리정의된
#   특별한 변수나 함수

# __name__ : 해당 파이썬 파일일 실행되면 main 이라는 값이 리턴
# 다른 파일의 import로서 사용되면.. 파일명이 리턴
# 모듈(함수들의 집합)을 만들때 

# dog 라는 클래스
# 변수는 age name을 정의하고 
# 함수는 : callDog  리턴값은 멍멍

# 객체 만들어서 사용
class Dog:
    # (),(20),(20,'멍뭉이'), (name='멍뭉이')
    def __init__(self,age=0,name=''):
        self.age = age
        self.name = name
    def callDdog():
        print("멍멍")

dog = Dog()
dog = Dog(1)
dog = Dog(1,'멍뭉이')
dog = Dog(name = '멍뭉이')
        
        