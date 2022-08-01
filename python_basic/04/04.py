# 순환문..... 조건을 만족할때 까지 순환
# 순환문 안에서 while의 조건을 변경하는 코드가 반드시 있어야 함
# 순환문이 다 돌기전에.... 내가 원하는 조건이되면 .. 강제로 순환문을 종료

# 10번 반복하는 도중에 count가 5가 되면 종료
count = 0
while count < 10:
    if(count == 5):
        break    
    print("수행할 로직")
    count += 1

# count가 5가 될때까지 무한히반복
count = 0
while True:
    if(count == 5):
        break    
    print("수행할 로직")
    count += 1    