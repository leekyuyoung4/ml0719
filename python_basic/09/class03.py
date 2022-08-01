# 클래스 : 변수와 함수를 묶어준다
# 입력(데이터) - 로직(비지니스 로직) - 출력(결과)


# 클래스
# 구구단을 출력
# 입력 : 단수를 입력을 받는다
# 로직 : 해당 단수의 구구단 만든다
# 출력 : 콘솔에 출력(세로,가로)

# 설계 : 순서도 - git 자료 ppt 참조

# 입력
# 예외처리 : 정수만 입력받을것.. 그리고 2~9사이의 숫자

# 숫자인지 문자인지 구분하는 isDigit
# 두 조건을 동시에 만족해야 true 가되는 조합은
# 조건1 & 조건2  : 조건1을 체크하고 그리고 조건2를 체크
# 조건1 and 조건2 : 조건1이 거짓이면.. 조건2를 체크안하고 바로 결과를 리턴
# 입력부분

# fuction description : 
# str : 물어볼 문자열
# start, end  : 허용하는 범위의 정수
def inputRangeInt(str,start, end):
    while True:
        num = input(str)
        if num.isdigit() and (start<=int(num)<=end):            
            return int(num)

dan = inputRangeInt("정수를 입력하세요(2~9) : ",2,9)
outOption = inputRangeInt("출력의 방향을 선택하세요(가로:1,  세로:2) : ",1,2)
# 구구단 로직 & 출력
if outOption == 2 :
    for i in range(1,10):
        print(f"{dan} x {i} = {dan*i}")
else:
    for i in range(1,10):
        print(f"{dan} x {i} = {dan*i}",end = "\t")
 ########################################################################       
class GuguDan:
    def exeGugudan(self):
        self.dan = inputRangeInt("정수를 입력하세요(2~9) : ",2,9)
        self.outOption = inputRangeInt("출력의 방향을 선택하세요(가로:1,  세로:2) : ",1,2)
        self.show()
    
    def inputRangeInt(self,str,start, end):
        while True:
            num = input(str)
            if num.isdigit() and (start<=int(num)<=end):            
                return int(num)
            
    def show(self):
        if outOption == 2 :
            for i in range(1,10):
                print(f"{dan} x {i} = {dan*i}")
        else:
            for i in range(1,10):
                print(f"{dan} x {i} = {dan*i}",end = "\t")
                


            

# while True:
#     num = input("정수를 입력하세요(2~9) : ")
#     if num.isdigit() and (2<=int(num)<=9):
#         print('ok')
#         break
#     else:
#         print("faile")        

# # 출력방향 선택
# while True:
#     outNum = input("출력의 방향을 선택하세요(가로:1,  세로:2) : ")
#     if num.isdigit() and (1<=int(outNum)<=2):
#     #if outNum.isdigit() and (int(outNum) == 1 or int(outNum) == 2):
#         print('ok')
#         break
#     else:
#         print("faile")        

