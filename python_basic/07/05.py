f = open('./7일차/text.txt','r',encoding='utf-8')
while  True:
    line = f.readline()   # ""
    if not line: break  # None          
    print(line,end="")
f.close()
