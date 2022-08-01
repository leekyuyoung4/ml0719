# 함수를 정의 default parameter
# 매개변수가 항상 변하지 않는다면... 초기값을 미리 설정하는것이 유리
def introduce(name, age, isman=True):
    gender = ''
    if isman:
        gender = '남'
    else:
        gender = '여'
    
    print(f"저의 이름은 {name} 이고 나이는 {age}, 성별은 {gender}")

# 함수호출
introduce("이규영",10,False)   

introduce("이규영",10)  

# TypeError: introduce() takes 3 positional arguments but 4 were given      
# introduce("이규영",10,True,True)        