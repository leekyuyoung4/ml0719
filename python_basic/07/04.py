f = open('./7일차/text.txt','r',encoding='utf-8')
# 1 번째 줄
print(f.readline())   

# ['2 번째 줄\n', '3 번째 줄\n', '4 번째 줄\n', '5 번째 줄']
print(f.readlines())  
f.close()
