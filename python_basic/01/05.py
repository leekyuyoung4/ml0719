# 문자열을 입력받고   - input()
# 찾고자하는 문자를 입력받아서
# 0000 문자열에서 0문자는 0번 나왔고 문자열의 총 길이는 0 입니다.

originalStr =  input("문자열을 입력하세요")
findch = input("찾고자 하는 문자를 입력하세요")

# 문자열 찾기
finedCount =  originalStr.count(findch)
# 문자열 길이
strleng = len(originalStr)

# 출력
result =  f'"{originalStr}" 문자열에서 "{findch}"문자는 {finedCount}번 나왔고 문자열의 총 길이는 {strleng} 입니다.'

print(result)

