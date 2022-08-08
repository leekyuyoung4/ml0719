# match
'''
group()     : 매치된 문자열을 돌려줌    
start()     : 매치된 시작위치
end()       : 매치된 문자열의 끝
span()      : 매치된 문자열의 (시작,끝) 튜플형태로
'''

import re
p = re.compile('[a-z]+')
m = p.match("pythone") # <re.Match object; span=(0, 6), match='python'>
print(m.group())
print(m.start())
print(m.end())
print(m.span())

m = p.search("3 python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())

