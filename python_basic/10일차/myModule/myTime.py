import time
print('5초간 정지합니다.')
for i in range(5):
    print(".",end="")
    time.sleep(1)
print('\n5초가 지났습니다.')