# 여러개의 오류 처리하기
from decimal import DivisionByZero

try:
    pass
except DivisionByZero as e:
    print(e)
except IndexError as e:
    print(e)
except Exception as e :
    print(e)
    
    
try:
    pass
except (DivisionByZero,IndexError) as e:
    print(e)
except Exception as e :
    print(e)    