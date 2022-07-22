# 자료구조 set 형태
# 집합 자료형  교집합 차집합 합집합
# add()  update()  remove()

# Bool 자료   Treu Fals만으로 구성되어 있는 자료형
# 조건 같은 연산자에 사용

print(1 == 1)
print(2 > 1)

# 자료형에 대한 조건문
#문자열    "phthon"       true
#           ""            false

#리스트    [1,2]          true
#           []           false
# 튜플이나 딕셔너리 도 값이 있으면 true   없으면 false

#숫자형     0           false
#          0을 제외한 모든 수  true
#           None        false         None이라는 값은 함수의 결과가 없을때 ... 

#bool() 함수  true/false를 판단
print( bool("phthon")  )  # true
print( bool("")  )        # false


# id()   메모리 주소를 확인
a = 100
print(id(a)) # 2230105869648

