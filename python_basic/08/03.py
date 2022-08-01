# 생성자...
# 클래스명 : Student
# 변수 : 이름 나이 학년 점수 학점
# 함수 : 학점계산  A B C D F
# 함수 : 학생정보 출력
#       문자열포멧을 이용해서 이름:000 나이:000 학년:00 점수:000 학점 :000
# 컴공과의 학생들 정보를 저장하고 사용해봅시다 - 객체를 원소로하는 집합을 생성
class Student:
    def setData(self, name,age,grade,jumsu):
        self.name = name
        self.age = age
        self.grade = grade
        self.jumsu = jumsu
        self.hakjum = None
    def calcHakjum(self):
        if(self.jumsu >=90):
            self.hakjum = 'A'
        elif(self.jumsu >=80):
            self.hakjum = 'B'
        elif(self.jumsu >=80):
            self.hakjum = 'C'
        elif(self.jumsu >=80):
            self.hakjum = 'D'
        else:
            self.hakjum = 'F'
    def show(self):
        print(f"이름:{self.name} 나이:{self.age} 학년:{self.grade} 점수:{self.jumsu} 학점 :{self.hakjum}")
# 클래스 사용
s = Student()  # 객체만들고
s.setData('홍길동',20,1,90) # 맴버변수를 새성하기위한 메소드

# 어자피 객체만 만들어서는 내부변수를 생성못해서 항상
# 객체생성후 변수생성하는 메소드를 호출
# 개선----->> 객체생성시 자동으로 메소드가 호출되게 하면 좋겠다
# 그래서 생성자라고 부르고 메소드 이름은 파이썬에서 정해줌
# 그 이름이  __init__(self, .....)


        
        
