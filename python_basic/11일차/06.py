# 사용자로부터 정수를 입력받아서 출력
while True:
    menu = """    1.회원가입
    2.회원탈퇴
    3.서비스 둘러보기
    4.종료"""
    print("메뉴를 선택해 주세요")
    print(menu)
    menuid = 0
    try:
        menuid = int(input("==> "))
    except:
        continue
    print(f"{menuid} 번을 선택하셨습니다.")
    break
    


    