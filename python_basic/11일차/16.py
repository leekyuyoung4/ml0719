# 파일명을 입력받아서 해당 파일을 열고 내용을  출력
# 이때 파일이없으면 파일이 없다고 출력
filename = input("파일명 : ")
f = None
try:
    f = open(filename,'r')
    print(f.read())
except FileNotFoundError as e:
    print("파일이 존재하지 않습니다. 경로를 확인해 주세요")
except Exception as e:
    print(f"다음과 같은 에러가 발생했습니다.{e}")    
finally:
    if f != None:
        f.close()