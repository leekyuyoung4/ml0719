# 함수를 정의
def introduce(name, age, isman):
    gender = ''
    if isman:
        gender = '남'
    else:
        gender = '여'
    
    print(f"저의 이름은 {name} 이고 나이는 {age}, 성별은 {gender}")

# 함수호출
introduce("이규영",10,True)   

# typeError: introduce() missing 1 required positional argument: 'isman' 
# introduce("이규영",10)  

# TypeError: introduce() takes 3 positional arguments but 4 were given      
# introduce("이규영",10,True,True)        