# 예외를 발생시키기

# print("예외발생시키기")
# raise ZeroDivisionError

# 06.py를 개선해서 
# 사용자가 숫자를 입력하고
# 입력한  숫자가 메뉴범위를 벗어난 숫자면
# 예외를 발생시킨다

try:
    pass
except Exception as e:
    print(e)

# 예외를 처리하는 클래스는 Exception
# 사용자 클래스를 Exception을 상속받아 만든다.-->예외클래스
class MenuIndexError(Exception):
    def __init__(self):
        super().__init__("1과 4사이의 메뉴를 선택하세요.")

try:
    menuid = 10
    if not(1 <= menuid <=4):        
        raise MenuIndexError()
    
except MenuIndexError as e:
    print(e)

