# 리스트 내포    데이터 분석
# 조건문을 사용   아래 리스트중에 짝수에만 3을 곱해서 리스트로 담는다
list_a = [1,2,3,4]
result = []
for i in list_a:
    if(i % 2 == 0):
        result.append( i*3)

# [6, 12]
result = [i*3 for i in list_a if i%2 ==0]
# [표현식 for 항목 in 반복가능객체 if 조건]


# for문 2개이상 사용가능
# [표현식 for 항목1 in 반복가능객체1 if 조건1
#         for 항목2 in 반복가능객체2 if 조건2           
# ......
# ]

# 구구단의 모든 결과를 리스트화
result = []
for i in range(2,10):
    for j in range(1,10):
        result.append( i*j)
        
result = [i*j for i in range(2,10) for j in range(1,10)]



