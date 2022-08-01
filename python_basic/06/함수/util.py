def introduce(name, age, isman=True):
    gender = ''
    if isman:
        gender = '남'
    else:
        gender = '여'
    
    print(f"저의 이름은 {name} 이고 나이는 {age}, 성별은 {gender}")


if __name__ == '__main__':
    introduce('홍길동',1000)    
