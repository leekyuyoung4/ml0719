# R 패키지
# 패키지 : 함수들을 기능별로 묶어놓은 일종의 꾸러미
#  공구함, 미술도구함, 조리도구함

#로딩(loading) : 패키지를 R에서 사용할 수 있도록 불러오는 작업

# 특정 패키지안에 있는 함수를 이용
# 1. 특정함수를 포함하고 있는 패키지를 설치(install)
# 2. 설치한 패키지를 불러오기(load)
# 3. 원하는 함수를 사용하기

# 명령문으로 패키지 설치하기
# install.packages()함수를 이용
# 예  ggplot2 패키지  설치
install.packages('ggplot2')
# ggplot2 불러오기
library(ggplot2)
# 사용하기
ggplot(data = iris,aes(x = Petal.Length,
                       y= Petal.Width)) + geom_point()

# 쉬어가는 코너
# cowsay 패키지를 설치
install.packages('cowsay')
library(cowsay)
say('Hello world', by='cat')

say('Hello world', by='snowman')
?sort
help("sort")

# 4가지 도움말 보는 방법
#1 gui
#2 F1
#3 ?함수명
#4 help(함수명)

# 과제
# ceiling()함수와 Sys.time()함수에대해 도움말 활용해서


# 5명  생일 맞추기 게임
# 태어난 달에 4를 곱하고, 그 결과에 9를 더하고 다시 그
#결과에 25를 곱하고 마지막으로  다시 그 결과에 태어난날짜를
# 더한다.

# a     b    c     d      f
# 931  754   1029  1139  14423
# 각자의 생일을 구해봅시다.

# 1수식을 만들어서 해당 수식의 의미를 파악
# ((m*4)+9)*25+d = 931

100m+225+d = 931
100m + d = (931-225)
# 100으로 나누었을대 몫이 m이고 나머지가 d
# ex)100*5 + 50 =  550
# a는 7월 6일

# 변수
total <-5050
total
print(total)
cat('합계 :',total)

num <-2,5
this-data<-10
this@data<-10
12th<-20
this is<-20

# 변수명 작명 규칙
abc<-850
mid.sum<-850  # 중간 합계 850를 저장한다.
student<-"이규영"
student.rank <-1 # student학생의 등급은 1등급

student
student.rank

# 자주사용하는 함수명을 변수로 하지 않는다
sqrt(120)
sqrt<- 340
sqrt



# 숫자형   : 정수 실수 모두 가능
# 문자형 :  ""   '' 
# 논리형 : TRUE, FALSE  T F
# 특수값 :  NULL   정의되어 있지 않음을의미 자료형도 없고 길이도0
#           NA   결측값(missing value)2
#           NaN  not a number  수학적으로 정의가 불가능한 값 sqrt(-3)
#           Inf(양의 무한대), -Inf(음의 무한대)  


age.1<- 20
age.2<- 30
age.1+age.2
name.1<-'john'
grade.1<= '3'
age.1 + grade.1  # 에러

5>3
T+F
T+T
F+F

1/0
-1/0
sqrt(-5)


# 소금물의 농도
# cat()함수를 이용해서 출력
"소금 = (), 물 = (), 농도 = ()"

#소금 50g과 물 100g을 섞었을때 소금물의 농도
salt<-50
water <-100
result <- salt / (salt + water)*100
cat("소금=",salt,"물=",water,"농도=",result)
