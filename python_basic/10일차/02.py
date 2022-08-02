# 클래스에서 변수를 생성하는 방법
# 1.클래스 변수(클래스안에 변수를 생성)
class Dummy:
    name = '홍길동'

# 클래스 변수 사용
#1. 클래스를 이용해서 사용
print(Dummy.name)

#2 객체를 이용해서 사용
d =Dummy()
d.name = '이순신'
print(d.name) # 이순신

Dummy.name ='강감찬'

d2 = Dummy()
print(d2.name)

print(Dummy.name)

    