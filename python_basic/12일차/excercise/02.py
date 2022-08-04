# 10 미만의 자연수 중에서 3과 5의 배수를 구하면 3 5 6 9 총합은 23
# 1000 미만의 자연수 중에서 3과 5의 배수의 총합

#1. 1000미만의 자연수 리스트
three = []
five = []
result = []
total = 0
for i in list(range(1000)):
    if i % 3 == 0 or i % 5 == 0:
        total += i
        
print(total)        

for i in list(range(1000)):
    if i % 3 == 0:
        three.append(i)
    if i % 5 == 0:
        five.append(i)    

print(sum(set(three+five)))
# print(sum(list(set(three) - set(five))))


# filter 를 이용해서 3과 5의 배수의 집합을 리스트로 추출한다음 합

filterdLists =  filter(lambda x : x % 3 ==0 or x % 5 ==0, range(1000))
print(sum(filterdLists))

num1 =  input("값을 공백을 이용해서 입력하세요")
# 확인용"100 200 300"
print(num1.split(" ")) # ['100','200','300']
# 공백을 통해 입력한 모든 숫자형 문자를 정수로 변환


