a = input('값을 입력하세요')
try:
    int(a)  # 정수만
    print("정수입니다.")
except ValueError as e:
    try:
        float(a)
        print("실수입니다.")
    except ValueError as e:
        print("특수문자를 포함한 문자입니다.")