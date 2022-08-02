class GuguDan:
    def __init__(self,dan = 2,outOption=2):
        self.dan = dan
        self.outOption = outOption
    
    def exeGugudan(self):
        self.dan = self.inputRangeInt("정수를 입력하세요(2~9) : ",2,9)
        self.outOption = self.inputRangeInt("출력의 방향을 선택하세요(가로:1,  세로:2) : ",1,2)
        self.show()
    
    def inputRangeInt(self,str,start, end):
        while True:
            num = input(str)
            if num.isdigit() and (start<=int(num)<=end):            
                return int(num)
            
    def show(self):
        if self.outOption == 2 :
            for i in range(1,10):
                print(f"{self.dan} x {i} = {self.dan*i}")
        else:
            for i in range(1,10):
                print(f"{self.dan} x {i} = {self.dan*i}",end = "  ")

if __name__ == '__main__':
    gugudan = GuguDan()
    gugudan.exeGugudan()