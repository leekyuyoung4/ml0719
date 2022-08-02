# 모듈로부터 가져오는 함수나  기타등등
# 중복이 되면 마지막에 가져온 함수나 변수가 최종적으로 사용된다.
from myModule.mod1 import *  # add() sub()
from myModule.mod2 import *  # CalcCircle   add()

result = add(10,2)
print(result)


# 실제사용예
from myModule.mod1 import add as myAdd
from myModule.mod2 import add

result = myAdd(10,2)
print(result)