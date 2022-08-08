import re

data = """
park 800101-1234567
kim 700101-1234567
"""

pattern = re.compile("(\d{6})[-](\d{7})")
print(pattern.sub("\g<1>-*******", data))

# 메타문자 : 문자그대로 사용하는게 아니라 특별한 용도로 사용하는 문자
# 정규식
# . ^ $ * + ? {} [] \ | ()

#[] 문자클래스 - character class
# [] 사이의 문자들과 매치
# [abc] : a b c 중 한개의 문자와 매치
# a   before  double  friend

#[a-c] : [abc]  [a-zA-Z]  
#[0-9]

# ^ : not  문자클래스 안에서 사용하면 not []
# [^a-zA-Z]  [^0-9]

# .  dot  \n을 제외한 모든 문자와 매치되는 메타문자
# a.b  a와 b사이에 \n을 제외한 어떤 문자가와도 매치
# aab  ajlsdjfoiejwjofib  매치
# ab  abb

# a[.]b   a.b문자열은 매치  aab 노매치

# * 반복  ca*t   caaaaaaaaaaaaat  0번이상 반복되면 매치
# ct  매치

# 반복 +  최소 1번이상
# ca+t   cat

# 반복 {m,n}  반복횟수가 m부터 n까지 매치 
# m , n은 생략이 가능
# {3, } 반복횟수가 3이상
# {, 3} 반복횟수가 3이하
# ca{2}t  caat
# ca{2,5}t  caat caaaaat

# ?  {0,1} 을 의미
# ab?c  b가 0~1번 사용되면 매치
# abc  ac

##########################################################################



