# list => index, slice
odd = [1,3,5,7,9]
temp = [1, 1.25, 'hello', odd, [1, 5, [2, 3.14] ] ]

# temp라는 리스트를 이용해서 리스트의 인덱스로 데이터를 가져온다... 
# hello
print( temp[2] )
# 3.14
findData = temp[4];
findData =  findData[2]
print(findData[1])
print(temp[4][2][1])

temp = [1,2,3,['a','b','c']]
temp[-1]
temp[-1][0]


# 리스트 연산
temp1 = [1,2,3]
temp2 = [4,5,6]
temp3 = temp1 + temp2

temp4 = temp1 * 3

# 리스트의 길이  len()
len(temp1)

temp = [1, 1.25, 'hello', odd, [1, 5, [2, 3.14] ] ]
print(len(temp))


# 리스트의 값을 수정
temp[-1] = 100
print(temp)   # [1, 1.25, 'hello', [1, 3, 5, 7, 9], 100]
# 삭제
del temp[-1]
print(temp)

# 자료구조는 CRUD 가 존재 합니다. 
temp.append(10)  # 마지막에 데이터를 추가
temp.insert(1,123)   # 원하는 위치에 추가
print(temp) # [1, 123, 1.25, 'hello', [1, 3, 5, 7, 9], 10]

# 정렬
temp = [1,5,8,2,10,7]
print(temp)
temp.sort() # 정렬의 기본은 asc 오름차순  반대는 desc 내림차순
print(temp.sort())
print(temp)

# 문자열중에 replace
strdata = "hello"  
modified =  strdata.replace('o',"")
print(modified)

sortedData = temp.sort();
print(f"sortedData = {sortedData}")


