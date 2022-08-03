try:    
    list_a = list(range(5))    
    print(f"list_a의 마지막 값은 {list_a[5]}")
    4 / 0
except ZeroDivisionError as e:
    print(f"에러가 발생했습니다. 에러의 유형은 : {e}")
except IndexError as e:
    print(f"에러가 발생했습니다. 에러의 유형은 : {e}")
    
# 4 / 0 # ZeroDivisionError: division by zero

print("프로그램 종료")