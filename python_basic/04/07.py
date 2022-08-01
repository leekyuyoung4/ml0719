# break.... continue
# to be continue......

# break는 순환문에 사용하면 그 즉시 탈출.

cnt = 0
while cnt < 10:
    if(cnt == 5):
        cnt += 1    
        continue

    print(f"{cnt}")
    cnt += 1

print("순환문이 종료되었습니다.")    