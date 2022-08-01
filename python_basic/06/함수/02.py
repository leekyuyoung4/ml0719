# 함수 입력 / 출력


import time


def add( a, b):
    return a + b

#출력만 있는 함수
def getTime():
    return time.strftime("%Y-%m-%d", time.localtime(time.time()))

#입력만 있는함수
def greeting( str ):
    print(f"{str}님 반갑습니다.")
    
# 입력과 출력이 모두 없는 경우
def seperateLine():
    print("====================================================")    

print( add(10,10))    
print(getTime())
greeting("이규영")
seperateLine()
