#   +, *, [], {}
# 매치가 진행될때 문자열의 위치가 변경되고.. 보통 소비된다

# 위치가 변경되지 않는 메타 문자
# |   or와 동일함
# A|B  A 또는 B
import re
p = re.compile("Crow|Servo")
m = p.match("CrowHello")
print(m)

# ^
# p = re.compile("^life", re.IGNORECASE)
# p = re.compile("[Life]")
p = re.compile("good$")
m = p.search("Life is good")
print(m)