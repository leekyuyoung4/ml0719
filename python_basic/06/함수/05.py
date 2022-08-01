# 람다
# 이름 없는 함수.

def explaine():
    print("더하기 함수 입니다. ")
    
def add ( a, b, func):
    func()
    return a+b    

print( add(10,20, explaine) )
# 더하기 함수 입니다. 
# 30
