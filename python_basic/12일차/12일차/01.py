# 내장함수

from random import sample


print(abs(-10))  # 절대값

# 논리연산자 중에 and와 비슷
# 집합중에 어느하나라도 false가 있으면전체가 false
print( all([1,2,3,4] ) ) # true
print( all([1,2,0,4] ) ) # false

# 논리연산자 중에 or와 비슷
# 집합중에 어느하나라도 true가 있으면전체가 true
print( any([0,0,1,0] ) ) # true
print( any([0,0,0,0] ) ) # false

print(chr(97))  # a

# 객체가 자체적으로 가지고 있는 변수나 함수반환
print( dir( [1, 2, 3] ) )
temp = [1,2,3]


print(divmod(5,2))  # 나눈 몫과 나머지를 튜플형태로 반환
d1,d2 = divmod(5,2)

#순서가 있는 자료형(리스타,튜플, 문자열) 받아서
# 인덱스값을 포함하는 enumerate 객체 반환 튜플형태로 반환
temp = ['body', 'hobby', 'study' ,1 ,10 ,100]

for idx, value in enumerate( temp):
    print(f"[{idx}] : {value}")

# eval은 문자열로 되어 있는 수식이나 명령어를 실제로 바꿔준다.
print ( eval("1+2") )

# inputData = input("값을 입력하세요")  # 12   12.56
# 정수 ->  실수 -> 문자
# print(type(eval(inputData)))
# try:
#     if type(eval(inputData)) is int:
#         print("정수")
#     else:
#         print("실수")    
# except Exception as e:
#     print("문자입니다.")

print(eval('divmod(5,2)'))

temp = [1,-8,20,5,7,-20]
print([i for i in temp if i< 0])


# def negative(x):
#     return x < 0

# print(list(filter(negative, temp) ))

print(list(filter( lambda x : x < 0, temp )))

# hex(x)  16진수로 변환
# id(object)   해당 객체의 주소값
# input()
# int()

class Person: pass

# 객체가 어느 클래스의 객체인지 판단
a = Person()
print(  isinstance(a, Person))  # true

# len(x)
# list(iterable)
print(list(range(5)))

# map  vs filter
# def twoTime(x):
#     return x**2
# temp = [1,2,3,4,5]
# print(list(map(twoTime, temp))) # [1, 4, 9, 16, 25]

temp = [1,2,3,4,5]
print(list(map(lambda x: x**2, temp))) # [1, 4, 9, 16, 25]

# pow(x, y)
# x를 y 제곱
print(pow(2,4))
print(2**4)

#sorted(iterable)
temp = sample(range(100),10)
print(f"before sorted {temp}")
print(sorted(temp))
print(sorted(temp,reverse=True))

# zip(literable, literable, ....)
print(list(zip([1,2],[10,20],['일','이']) ))