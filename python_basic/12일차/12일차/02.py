# 라이브러리
# sys.path  파이썬 모듈을 불러올때 사용
import sys

sys.path.append("D:/이규영강사/이규영강사/workspace/myModule/mod1.py")
#from myModule.mod1 import add
# print(add(10,20))
# 객체를 파일에 저장하고 파일에사 다시 읽어서 객체로 사용

import pickle
with open("test.txt", 'wb') as f:
    data = {1:'python', 2:"best choice"}
    pickle.dump(data,f)

    

