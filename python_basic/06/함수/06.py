def add(a,b):
    return a+b

def minus(a,b):
    return a-b

def calc(a,b,calfunc):
    return calfunc(a,b)


# 사용
print( calc(10, 20, add) )
print( calc(10, 20, minus) )

a,b = 10,20

c = a+b
print(c)

