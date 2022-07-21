temp = 1

#파이썬에서는 모든 변수는 object 즉 객체라고 불러요..
# 클래스로부터 만들어진다...
# .  dot operation  맴버연산자.

temp = [1,5,8,2,10,7]
# 오름차순 정렬
temp.sort()
print(temp)  # [1, 2, 5, 7, 8, 10]

#내림차순 정렬
temp.sort(reverse=True)
print(temp)  # [10, 8, 7, 5, 2, 1]

#순서를 뒤에서 부터 출력
temp.reverse()
print(temp)
# [1, 2, 5, 7, 8, 10]

del temp[1]  # 인덱스 기반의 삭제 방법
temp.remove(5) # 원하는 값을 찾아서 삭제한다.
print(temp)   # [1, 7, 8, 10]
# pop 
print(temp.pop())   # 10
print(temp)   # [1, 7, 8]

print(temp.pop(1))  # 7
print(temp)   # [1,  8]

# len() vs 데이터.count(값)
temp = [1, 2, 5, 7, 5, 10]
print(temp.count(5))

# 리스트 + 리스트
list01 = [1,2,3]
list02 = [4,5,6]
list01.extend(list02)  # 원본이 변경됨
print(list01)

# list01 =  list01 + list02   # 38번 라인과 동일
list01 += list02
list01 = list02

a = 0
a += 1
a += 2
a += 3
a += 4
a += 5
# 마지막 a는 무슨값일까?  15
a -= 1
a -= 2

a *= 1
a *= 1

a /= 1
a /= 2

# a = a / 2

a = 0

a += 1 
a += 1 
a += 1 
a += 1 
a += 1 
