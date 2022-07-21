# 공백을제거 하는 함수
# strip()  양쪽
# rstrip()  오른쪽
# lstrip()  왼쪽
origin1 = "abc"
origin2 = " abc"  # 빅데이터 분석할대. 데이터수집을 하다보면... 공백과 같은 ..
print(origin1)
print(origin2)
print(origin2.strip())

# 문자열 대체  replace()
origin3 = "가나다라마바사"
origin3 = ",".join(origin3)
print(origin3)
print(origin3.replace(",",""))

# 문자열 분리 split()  -> 리스트를 만들어줌

# origin3 -->가,나,다,라,마,바,사
origin_split = origin3.split(",")
print(origin_split)   # ['가', '나', '다', '라', '마', '바', '사']   리스트

# 사실 리스트는 우리가 공부함  문자열을 그 자체가 하나의 리스트형태

print(origin_split[:3])  # ['가', '나', '다']

# 퀴즈....  ['가', '나', '다'] 결과를  "가나다"

temp =  origin_split[:3]
print(temp[0]+temp[1]+temp[2])


