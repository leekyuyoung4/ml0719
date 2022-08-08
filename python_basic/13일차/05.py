# 정규식의 컴파일 옵션
data ='''
DOTALL      S   dot문자 .가 \n을 포함해서 모든 문자와 매치
IGNORECASE  I   대소문자를 무시하고 매치  
MULTILINE   M   여러줄과 매치
VERBOSE     X   verbose 모드를 사용
'''

import re
p = re.compile('a.b',re.DOTALL)
m = p.match('a\nb')
print(m)

p = re.compile('[a-z]',re.IGNORECASE)
m = p.match('Python')
print(m)


data ='''python one
hello
python two
good
python three
morning
'''
# ^ : 문자열의 처음
# $ : 문자열의 마지막
p = re.compile('^python\s\w+',re.MULTILINE)
print(p.findall(data))



