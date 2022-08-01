#생성자. 객체생성시 자동으로 호출
#생성자에 코딩하는 내용은 주로 내부변수 생성 및 초기화

# 학생클래스를 만들고  학생을 관리...
# 어떤학급.. 정원이 15명  을 관리할 자료구조를 선택하고 거기에
# 저장하고 불러온다.




class Student:
    def __init__(self,name,age,grade,jumsu=None,addr=None):
        self.name = name; self.age =age; self.grade = grade
        self.jumsu = jumsu; self.addr = addr; self.hackjum = None
    def calcHack(self):
        if self.jumsu >=90:
            self.hackjum = 'A'
        elif self.jumsu >=80:
            self.hackjum = 'B'
        elif self.jumsu >=70:
            self.hackjum = 'C'
        elif self.jumsu >=60:
            self.hackjum = 'D'
        else:
            self.hackjum = 'F'
    def showInfo(self):
        print(f"이름:{self.name} 나이:{self.age} 학년:{self.grade} 점수:{self.jumsu} 학점:{self.hackjum} 주소:{self.addr}")

students = [ 
            Student('홍길동1',35,1,95,'서울시1'),
            Student('홍길동2',36,1,85,'서울시2'),
            Student('홍길동3',33,1,75,'서울시3'),
            Student('홍길동4',15,1,65,'서울시4'),
            Student('홍길동5',27,1,55,'서울시5')
            ]        
    

# 모든학생들의 학점을 구하고 
for student in students:
    student.calcHack()
    print(f"{student.name} : {student.hackjum}")    
# 학생 : A  이런식으로 모든 학생의 학점을 출력
# Q 학점순으로 출력  (오름차순, 내람차순)
# 최고 학점 학생정보출력
# 리스트에 있는 학생들의 평균
# 정보를 화면에출력하는거 대신에 파일에 저장

# 아래출력처럼 이름:학점 의 형태를 가지는 자료구조를 만들어서
# 저 구조를 저장
# 학생리스트를 하나더 만들어서 ex) student1 VS student2
# 두개 그룹에서 동일한 점수를 가지는 학생정보를 출력  set()
# 동일한 점수를 배제한 정보를 출력      set()


