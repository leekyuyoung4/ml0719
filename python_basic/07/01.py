# 파일 입출력
# 파일객체 =  open(파일이름, 파일열기모드)
# r  읽기모드 - 읽기만 할때 
# w  쓰기모드 - 내용을 기록할때
# a  추가모드 - 파일의 내용을 읽어서 마지막에 내용 추가

print("안녕하세요\n반갑습니다.")

# f = open('./7일차/text.txt', 'r', encoding='utf-8') # 상대 경로
f = open('/text.txt', 'r', encoding='utf-8') # 상대 경로

#f = open('D:/text.txt' , 'r',encoding= 'utf-8') # 절대경로
line =  f.readline()
print(line)

f.close()  # 파일은 리소스의 개념 반드시 close()  Database

