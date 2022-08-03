# raise를 이용
# 클래스에서 특정 값이 들어오면 예외발생
class MyException(Exception):
    # def __init__(self, *args: object):
    #     super().__init__("사용할수 없는 별명입니다.")
    def __str__(self):
        return "사용할수 없는 별명입니다."

class NickName:
    def __init__(self, nick='별명없음'):
        if nick == '바보':
            raise MyException
        self.nick = nick
    def showNickName(self):
        return self.nick
    
# 사용
try:
    a = NickName('호랑이')    
    b = NickName('바보') # 별명이 바보이면 예외를 발생시켜라 이때 예외는 사용자 정의 예외를 만들어서 발생시킬 것
    print(a.showNickName)
    print(b.showNickName)
except Exception as e:
    print(e)