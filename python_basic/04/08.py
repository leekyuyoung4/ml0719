# 0 ~ 10 중에 홀수만출력  while문에서 continue를 이용  hint : 5만 제외하고 출력
# 1
# 3
# 5
# 7
# 9

cnt = 0
while cnt<=10:
    if(cnt % 2 == 0):
        cnt += 1
        continue    
    print(f"{cnt}")
    cnt +=1
    