# try ~ except ~ finally
# try 구문에서 예외가 발생하면 except 구문에서 처리
# finally는 최종적으로 마지막에 반드시 해당 구문이 실행
# 예를들어 파일 입출력.. with 구분없이....
try:
    f = open('test.txt', 'w')
    f.write("hello")
    # 4 / 0
    print("try문 정상 실행")
except:
    print("예외처리")
finally:
    f.close()
    print("finally 문장 실행")
    