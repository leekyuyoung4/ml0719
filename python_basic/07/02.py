# 함수.. 파라메터, default parameter
# parameter를 지정해서 전달하기

def showPersonInfo(name, age, gender='여', addreess='서울시'):
    print(f"이름 : {name}, 나이:{age} 성별:{gender} 주소:{addreess}") 
    
showPersonInfo("홍길동",100, "경기도")    
showPersonInfo("홍길동",100, addreess="경기도")    
    
    