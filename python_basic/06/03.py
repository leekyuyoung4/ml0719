for i in range(1,6):
    for j in range(i):
        print("*", end="")
    print()

# 위의 직각삼각형을 역순으로 출력
for i in list(range(1,6))[::-1]:
    for j in range(i):
        print("*", end="")
    print()
    

# Q1 아래와 같이 출력을 만들어 봅시다.. for문 두개사용해서.
#    *
#   ***
#  *****
# *******    