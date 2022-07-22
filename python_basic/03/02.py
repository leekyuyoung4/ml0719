# 사전 만들기
# 월 화 수 목 금 토 일
weeks = {'mon' : "", 'tue':'화', 'wed' : '수', 'thu' : "목", 'fri' : '금', 'sat' : '토', 'sun':'일' }

# Q1 sat의 값을 출력  - 2가지 방법 사용  get()  / key값 을 이용
print(weeks.get("sat"))
print(weeks['sat'])

# Q2 모든 키값을 출력
print(list(weeks.keys()))

# Q3 모든 벨류 값을 출력
print(list(weeks.values()))

# Q4 mon 의 값을 조회할때 항상 '월' 이 출력되도록
print(weeks.get('mon','월'))

# Q5 특정 키가 있는지 확인  'sunday'
print('sunday' in weeks)

# Q5  'sunday' 라는 키와 적당한 값을 추가
weeks['sunday'] = '일'

print(weeks) # {'mon': '', 'tue': '화', 'wed': '수', 'thu': '목', 'fri': '금', 'sat': '토', 'sun': '일', 'sunday': '일'}
