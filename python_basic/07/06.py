# read 함수 사용하기 파일전체내용을 문자열로 반환
f = open('./7일차/text.txt','r',encoding='utf-8')
data = f.read()
print(data)
f.close()