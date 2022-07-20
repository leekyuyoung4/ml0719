# 문자열 포멧팅 f 사용법
# 파이썬 3.6 도입
from itertools import count


name = "이규영규영"
hobby = "게으름피우기"

print(f"당신의 이름은 : {name} 이고 취미는 {hobby} 입니다.")

# 문자열 관련 함수   --> 함수의 모양   이름(매개변수 또는 아큐먼트 또는 파라메터)
# count() vs len()
# count() 문자열 안에서 해당 문자의 출현 횟수
# len()  문자열의 전체 길이(개수)

# 이름 --> 변수
# 이름() --> 함수
findChar = '규'
print(f"'{name}'문자열에서 '{findChar}'의 횟수는 {name.count(findChar)} 입니다. ")
print( f"'{name}'의 문자열 길이는 {len(name)} 입니다. " )
