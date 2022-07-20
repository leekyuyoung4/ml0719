# find()   찾고자 하는 문자가 문자열에 있으면 그 위치를 반환
# 없으면 -1을 반환

# count() VS find()
original = "Phthon is the best!"
print(original.count('i'))   # 1
print(original.find('i'))    # 7  --> 인덱스를 반환

print(original[7])  # i

# index()  find()와 기능을 동일하지만.... 찾지 못하면 에러
# 에러가필요하때가 있음... 프로그램이 죽어야만 할때가 있음

# join() 문자열을 특정 조건에따라 합친다.

# 가나다라마바사  -> 가,나,다,라,마,바,사

print(",".join("가나다라마바사"))
print("abc".join("123"))  # 1abc2abc3

# upper()  lower()

print(f"원본문자{original}  대문자로변환:{original.upper()}  소문자로 변환:{original.lower()}  변환후 원본문자 : {original}")

# upper / lower   검색또는 사용자로 부터 값을 받았는데.. 프로그램상에서 대소문자 구분이 되어 있을때 대소문자 상관없이 처리하고자 할때 사용



