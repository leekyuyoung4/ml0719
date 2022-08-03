# 리스트에 있는 모든 정수 및 실수를 포함한 모든 숫자의
# 합을 구해보세요.


list_a = list(range(5)) + ['a','b','c'] + [12.3, 15.9]
print(list_a)
# [0, 1, 2, 3, 4, 'a', 'b', 'c', 12.3, 15.9]
result = 0
for data in list_a:
    if (type(data) is int)  or (type(data) is float):
         result += data

print(result)

# try ~ except
result = 0
for data in list_a:
    try:
        result += data
    except:
        pass
print(result)    
    