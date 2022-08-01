# 커피 : 300
# 유자차 : 200
# 우유 : 100
# 컵은 입력을 받는다.
# 커피를 다 판매했을때.... 결산....
# 커피는 00잔, 유자차 00잔  우유00잔... 총 수입금액은 000
cups = int(input("자판기 셋팅 컵의수는 : "))
products = [0,0,0,0]  # index 1 coffe, 2 yja  3 milk
produectType = [0,300,200,100]
totlaPrice = 0
while cups > 0:
    choiceMenu = int(input("메뉴를 고르세요(1.커피:300, 2.유자차:200, 3.우유:100"))
    products[choiceMenu] += 1  
    totlaPrice += produectType[choiceMenu]
    cups -= 1
    if(cups == 0):
        print("판매중지")
        break

print(f"커피는 {products[1]}잔, 유자차 {products[2]}잔  우유{products[3]}잔... 총 수입금액은 {totlaPrice}");

    



