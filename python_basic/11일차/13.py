# try ~ except
# 상속

#1. try~except 사용해 보기
#2. try~except~finally 사용해 보기
#3 tyr~ except 예외결과 출력하기 as 이용

import time
count = 0
try:
    while count < 10:
        print(count,end=" ", flush=True)
        count += 1
        time.sleep(1)
    print("프로그램 정상 종료")
except KeyboardInterrupt:  # ctrl+c
    print("\n사용자에 의해 프로그램이 종료되었습니다.")