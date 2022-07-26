# range 함수 list함수와 같이 사용  순차적인 정수리스트를

print(range(10))  # range(0, 10)
print( list(range(10)) )  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print( list(range(10,20)) ) # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# Q1 아래 리스트에서 값을 추출해서 1,2,4,5,6 을 요소로하는 리스트를 만들어 보세요.
listData = [1,2,'a','b','c',[4,5,6]]

print(listData[:2]+listData[5])  
# TypeError: unsupported operand type(s) for +: 'int' and 'list'

#Q2 태양계에서 지구는 몇번째에 있는지 출력
solarArray = ['수성','금성','지구','화성','목성','토성','천왕성','해왕성','명왕성']
hangsung = "지구"
earthIndex = solarArray.index(hangsung)
# 지구는 태양에서 00번재 위치하고있습니다.
print(f"지구는 태양에서 {earthIndex}번재 위치하고있습니다.")  
print(f"지구는 태양에서 {solarArray.index('지구') + 1}번재 위치하고있습니다.")  
print(f"지구는 태양에서 {solarArray.index(hangsung) + 1}번재 위치하고있습니다.")  


