tuple01 = ('abc',123)

# 변수를 만드는 다양한 방법

# a,b = ('abc',123)
# (a,b) = 'abc',123
#(a,b) = ('abc',123)

# a,b = ['abc', 123 ]
# [a,b] = 'abc', 123 
#[a,b] = ['abc', 123 ]

a,b = 'abc', 123
print(a)
print(b)

# 변수를 서로 변경할때는 위의 기능을 이용한다.
# 변수 초기화( 최초 값이 할당되는 것을)
a = 100
b = 200
print(f"a는 {a}이고 b는 {b}입니다.")
print("두 변수의 값을 서로 교환한후 ")
# 두개의 변수의 값을 교환하는 코드 작성
# temp = a
# a = b
# b = temp

a, b = b, a




print(f"a는 {a}이고 b는 {b}입니다.")

