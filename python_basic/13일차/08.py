# 문장에서 특정단어가 몇번 나왔는지 빈도수 구하는 함수
data = '''
[SBS 연예뉴스 | 김지혜 기자] 영화 '리미트'(감독 이승준)가 8월31일로 개봉을 확정했다.

'리미트'는 아동 연쇄 유괴사건 피해자 엄마의 대역을 맡은 생활안전과 소속 경찰 '소은'(이정현)이 사건을 해결하던 도중 의문의 전화를 받으면서 최악의 위기에 빠지게 되는 범죄 스릴러. 이 영화는 당초 8월 17일 개봉을 예정했으나 일정을 2주 미뤄 8월 31일 개봉을 확정했다.

이 작품은 이정현, 문정희, 진서연의 연기 대결로 기대를 모으고 있다. 여기에 박명훈, 최덕문, 박경혜 등 충무로 대표 신스틸러들이 가세했다.

일본 추리 소설의 대가 故 노자와 히사시의 원작 소설을 기반으로 한 탄탄한 스토리텔링에 한국적 감성이 더해진 스릴러로 기대를 모으고 있다.

ebada@sbs.co.kr

ⓒ SBS & SBS Digital News Lab 무단전재 및 재배포 금지
'''

# 1. '위'  '위기'

findStr = "위기"
import re
p = re.compile(f"[{findStr}]+")
m = p.findall(data)
print(m)
print(len(m))