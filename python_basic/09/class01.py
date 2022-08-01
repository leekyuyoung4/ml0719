# 변수
# 자료구조 - 리스트, 튜플, set, dictionary
# 함수 - 명령어들의 집합 - 모듈화
# 조건문 - if ~ else
# 순환문 - for(횟수 -range() , 자료구조 ), while(특정조건을 만족..)
# 클래스 - 새로운 사용자 정의 테이터타입 or 자료구조
#        - 변수, 함수
#        - 생성자  __init__  : 객체를 생성시 자동으로 호출되는 함수
#        - 함수의 모든 parameter 중에 첫번째가 self를 사용한다

# 일반함수(클래스에 속하지 않은)

def showInfo():
    print("함수 고양이 입니다.")    

# 클래스를  생성(빈껍대기)    
class Cat:    
    def __init__(self,age=0,name=''):
        self.age = age
        self.name = name
        print("생성자가 호출되었습니다. ")
        
    def showInfo(self):  # 맴버함수는 반드시 self 파라메터를 가지고 있어야 함
        print("클래스 고양이 입니다.")


# 함수호출
showInfo()

# 객체 생성 - 변수처럼 namming .(dot)연산자를 통해서
# 클래스 안에 정의한 변수나 함수를 사용
# 객체를 생성할때는  클래스명() 를 호출해서
# 적당한 변수에 담으면 그 변수는 객체
# 이때 생성자(이름이 정해져 있는 함수)가 자동으로호출된다
a = Cat() # __init__(self)
a.showInfo()

# 함수 고양이 입니다.
# 생성자가 호출되었습니다. 
# 클래스 고양이 입니다.
# 변수는 객체를 생성한 이후에도 만들수 가 있음 - 클래스의 맴버가 아님
a.age = 10  # 임시변수
a.name = '나비'
print(a.age)
print(f"name:{a.age} / age:{a.name}")

b = Cat(1,'야옹이') # __init__(self,1,'야옹이')
print(f"name:{a.age} / age:{a.name}")

# age, name 필요
