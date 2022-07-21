# 튜플.. Tuple  리스트와 유사
#  만든법이 다르다.
# 리스트는 프로그램이 실행되는 동안.. 값이 변경가능
# 반면에 튜플은 한번 만들면 변경이 불가능
# 굳이 변경을 해야하 한다면 리스트로 변경한 새로운 변수를만들어서 사용

list01 = [1,2,3]  # 리스트
tuple01 = (1,2,3) # 튜플
tuple01 = ()
tuple01 = (1,)   
tuple01 = 1,2,3,4
tuple01 = (1,2,3,4, ('a','b') )
print(tuple01[0])
print(tuple01[:3])
print(tuple01[-1])

# del tuple01[0]   # error
# tuple01[0] = 100 # error

tuple01 = (1,2,3)
tuple02 = (4,5,6)
tuple03 = tuple01 + tuple02
print(tuple03)
print(tuple03 * 2)

# 튜플을 리스트로 변경
print(list(tuple03))   # [1, 2, 3, 4, 5, 6]
changeList = list(tuple03)



