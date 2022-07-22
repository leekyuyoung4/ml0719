# 파이썬 자료구조 리스트 []  / 튜플 () / 딕셔너리 {}
# 딕셔너리 : (map, json) 와 유사항 형태   키:값

dic = {'name' : '홍길동', 'phone' : '000', 'birth' : '1118' }
dic2 = {'age' : 100}
dic3 = { 'students' : ['홍길동','이순신','유관순'] }

print( dic['name'] )  # read  

dic['address'] = '서울시'  # 해당 키가 없으면 새로 생성하고 키가 있으면 해당하는 값을 변경

print(dic)  # {'name': '홍길동', 'phone': '000', 'birth': '1118', 'address': '서울시'}

dic["name"] = '철이'
print(dic) # {'name': '철이', 'phone': '000', 'birth': '1118', 'address': '서울시'}

del dic["name"]
print(dic) # {'phone': '000', 'birth': '1118', 'address': '서울시'}

# dictionary 를 위한 함수   함수:기능을 모아놓은 곳

# keys() --> dictionary key값만 출력
print(dic.keys() ) # dict_keys(['phone', 'birth', 'address'])

dicKeys = list( dic.keys() )
print(dicKeys)  # ['phone', 'birth', 'address']

# values()
print(dic.values()) # dict_values(['000', '1118', '서울시'])
dicValues = list(dic.values())
print(dicValues) # ['000', '1118', '서울시']

# items()  key와 value의 쌍을 튜플로 묶은 값들의 집합  
print(dic.items()) #dict_items([('phone', '000'), ('birth', '1118'), ('address', '서울시')])
dicItems = list( dic.items() )
print(dicItems) #[('phone', '000'), ('birth', '1118'), ('address', '서울시')]
print(dicItems[0][1])

# clear()  모든 요소를 삭제
dic.clear()
print(dic) #{}


# in  dictionary 에서 key가 존재하는 지 확인  true  false
dic = {'name' : '홍길동', 'phone' : '000', 'birth' : '1118' }

print('name' in dic) # true
print('names' in dic) # false

# get()  key에 해당하는 값을 반환    dic['name']
# get() vs dic['name'] 
# dic['name']  --> 해당 키 값이 없으면 error
# get() 키 값이 없으면 None을 반환, 만약에 값이 없으면 지정....즉 default 개념

# print(dic['address']) # KeyError: 'address'
# print(dic.get('address'))  #  None

print(dic.get('address','조선') )  # 값이 없으므로 default 조선이 출력




