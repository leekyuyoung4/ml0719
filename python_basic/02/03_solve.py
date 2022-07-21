# 특정 위치의 문자 출력하기
txt01 = "오늘은 목요일 입니다."
txt02 = "내일은 금요일 입니다."

# Q1  txt01에서 목요일 을 추출해 보세요.
print(txt01[4:7])
# Q2  txt02에서 금요일 을 추출해 보세요.
print(txt02[4:7])
# Q3  txt01 역순으로 출력해보세요  - 문자열을 리스트로 만들고 리스트의 함수를 이용
test =  [item for item in txt01]
test.reverse()
print("".join(test))   
    
    
# Q4  txt01 과 txt02 문자열을 합쳐 보세요
print(txt01 + txt02)

list01 = [1,2,3,4,5,6,7,8,9,10]
# Q5  list01 홀수만 출력  [1,3,5,7,9]
print(list01[::2])
# Q6  slice를 이용해서 txt01 을 역순으로 출력
print(txt01[::-1])

filename = input("저장할 파일명을 입력하세요 :")
filename += ".jpg"
# 당신이 입력한 파일명은 : 000000 입니다.
print(f"당신이 입력한 파일명은 : {filename} 입니다.")
print("당신이 입력한 파일명은 : %s 입니다." % filename)
print("당신이 입력한 파일명은 : " + filename +  " 입니다.")


# Q7  txt01의 문자열 길이
print(len(txt01))
# Q8 Q4에서 합친 문자열중에서 '일' 이라는 단어는 몇개 나왔는지 세어보세요
print((txt01 + txt02).count("일"))

txt03 = "Hello How Are You"
# Q9 txt03를 전부 대문자 또는 소문자로 변경 
print(txt03.upper())
print(txt03.lower())
# Q10 txt03 공백을 기준으로 분리해서 리스트로 만들것
splitList = txt03.split(" ")
print(splitList)