#다른 문장
# while true:
#   수행할 문장
#   수행할 문장
#   수행할 문장
#   수행할 문장

#다른 문장
print("순환문 진입 전")    

# Q1 아래 무한loop를 수정해서 10번만 실행되도록
# 무한 loop  
count = 0
while count < 10:
    print(f"순환문 문장 실행 count : {count}")    
    count += 1  #변수의 값을 순환문이 실행될때마다 1씩 증가

print("순환문 종료")    