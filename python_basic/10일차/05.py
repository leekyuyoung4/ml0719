import gugudan

# 클래스 exeGuguda은 gugudan.py에 있는 GuguDan 클랫를 상속
# 기존 클래스를 이용해서 구구단 전체를 출력하는 기능
# 부모의 맴버를 자식에서 사용할때.. 변수는 self.     
# 메소드는 self.   또는 super().   으로 호출함
# 자식에서는 부모의 모든 요소를 내부에 객체로 가지고 있기때문에
# self.000 으로 사용한다

class GugudanPlus(gugudan.GuguDan):    
    def showAllGugudan(self,option = 2):
        for i in range(2,10):
            self.dan = i
            self.outOption = option
            self.show() 
            print()           
            
gugudanplus =  GugudanPlus()
gugudanplus.showAllGugudan(3)