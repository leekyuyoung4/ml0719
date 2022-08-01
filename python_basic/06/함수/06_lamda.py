# 람다는 이름없이 정의하는 함수로 이름이 없으니 재사용 불가능
# lambda 매개변수: 로직



# def add(a,b):
#     return a+b
# add = lambda a,b: a+b

# def minus(a,b):
#     return a-b
# minus = lambda a,b: a-b

def calc(a,b,calfunc):
    return calfunc(a,b)

# 사용
print( calc(10, 20, lambda a,b: a+b ) )
print( calc(10, 20, lambda a,b: a-b ) )
print( calc(10, 20, lambda a,b: a*b ) )
print( calc(10, 20, lambda a,b: a/b ) )
