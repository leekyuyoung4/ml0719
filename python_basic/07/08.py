#  with  절을 이용하면 자동으로 닫힌다 
with open('temp2.txt', 'w', encoding='utf-8') as f:
    f.write("파일이 열려있는 동안 파일 핸들링을 하고\n")
    f.write("블록을 벗어나면 자동으로 닫힌다.")
    