# 요금 계산기..
# 1. 성인은 할인 없음 2. 어린이는 50%할인  청소년은 30%할인
# 기본 요금은 10000원
# 성인 클래스  Adult
# 어린이 클래스  Child
# 청소년 클래스 TeanAger

#1.  상속기능을 통해 메소드를 override 
class Adult:
    # 요금지불
    def payEnter(self):
        return 10000

# 성인 요금의 50%할인
class Child(Adult):
    def payEnter(self):
        return 5000
    

# 성인  요금의 30% 할인 
class TeanAger(Adult):
    def payEnter(self):
        return 7000

enters = [ Adult(),Adult(),Adult(),Adult(),Child(),Child(),Child(),TeanAger(),TeanAger(),TeanAger(),TeanAger()]

# 총 입장 금액
totalPrice = 0
for i in enters:    
    totalPrice += i.payEnter()    

print(f'총 입장금액 : {totalPrice}')        

