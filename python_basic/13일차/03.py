import re
p = re.compile('[a-z]+')
'''
p.match()       : 문자열의 처음부터 정규식과 매치되는지 조사 
p.search()      : 문자열 전체
p.findall()     : 매치되는 모든 문자열을 리스트로 돌려          list(range(10))
p.finditer()    : 매치되는 모든 문자열을 반복가능한 객체로 돌려  range(10)
'''


m = p.match("python program")
print(m)

m = p.match(" python program")
print(m)

m = p.match("3python program")
print(m)

m = p.search("3python program")
print(m)

m = p.findall("3python program")
print(m)

m = p.finditer("3python program")
print([i for i in m])