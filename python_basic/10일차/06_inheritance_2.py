# 요금 계산기..
# 1. 성인은 할인 없음 2. 어린이는 50%할인  청소년은 30%할인
# 기본 요금은 10000원
# 성인 클래스  Adult
# 어린이 클래스  Child
# 청소년 클래스 TeanAger

#2. 상속을 통해서 부모의 함수를 자식에서 호출
from itertools import count


class Adult:
    # 요금지불
    def payEnter(self,rate = 1):
        return 10000*rate

# 성인 요금의 50%할인
class Child(Adult):
    def payEnter(self):
        return super().payEnter(0.5)
    

# 성인  요금의 30% 할인 
class TeanAger(Adult):
    def payEnter(self):
        return super().payEnter(0.7)

enters = [ Adult(),Adult(),Adult(),Adult(),Child(),Child(),Child(),TeanAger(),TeanAger(),TeanAger(),TeanAger()]

# 총 입장 금액
totalPrice = 0
for i in enters:    
    totalPrice += i.payEnter()    

print(f'총 입장금액 : {int(totalPrice)}')

# 83,000 원 출력 해 보기
# int -> str 로 변경해서
# 뒤에서부터 꺼꾸로 읽어서 3자리마다 ,를 추가해서 하나의 스트링을 만들면됨
# 꺼꾸로 읽는 거는 index slice를 이용

#1. 결과를 문자열로 만든다.. 이때 실수형태는 정수로 만들고
strTotalPrice =  str(int(totalPrice))
reverse_strTotalPrice = strTotalPrice[::-1]  # 00038
makePrice = ''

for i in range(0, len(strTotalPrice)):
    if i % 3 == 0:
        makePrice += ','    
    makePrice += reverse_strTotalPrice[i]

print(makePrice[1:][::-1])    
    