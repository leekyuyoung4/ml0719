# import myModule.mod1
# result = myModule.mod1.add(10,20)
# print(result)

# import myModule.mod1 as mm
# result = mm.add(10,20)
# print(result)

# 사이킷런의 라이브러리를 가져올때 많이 등장
# from myModule.mod1 import add
# resutl = add(10,20)
# print(resutl)

# 전부 가져올때는
from myModule.mod1 import *
print(add(10,20))
print(sub(10,20))

