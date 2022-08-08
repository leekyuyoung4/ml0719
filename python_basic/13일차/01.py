data = """
park 800101-1234567
kim 700101-1234567
"""
# 문자열중에 주민번호 뒷자를 찾아서 *로 변경해서 출력
# 1. 공백을 기준으로 나눈다
# 2. 나눈 단어가 주민번호형식인지 조사(문자열의 길이가14, 앞에서부터 6 숫자, 7부터 마지막까지가 숫자)
# 3. 그 단어가 주민번호 형식이면 뒷자리를 *로 변환한다
# 4. 나눈 데이터를 다시 조립한다.
print(data)
print('--------------------------------------------')
result = []
for line in data.split("\n"):  # park 800101-1234567
    inner_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + '-' + '*******'
        inner_result.append(word)          
    result.append(" ".join(inner_result))

print('\n'.join(result))