f = open('./7일차/text.txt','r',encoding='utf-8')

lines = f.readlines()
# print(lines)
#['1 번째 줄\n', '2 번째 줄\n', '3 번째 줄\n', '4 번째 줄\n', '5 번째 줄']
for i in lines:
    print(i,end='')

f.close()