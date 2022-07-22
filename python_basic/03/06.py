# 점수를 입력하면 학점을 알려주는 프로그램  
# 100 ~ 90 : A
# 89 ~ 80 : B
# 79 ~ 70 : C
# 69 ~ 60 : D
# 59 ~ 0 : F

pocket = ['paper', 'cellphone']
card = True
# 주머니에 돈이 있으면 택시를 타라
# if 'money' in pocket:
#     print("택시를 타고 가자")
# else:
#     print("걸어갑시다")

# 주머니에 돈이 있으면 택시를 타고 만약에 없는데. 카드가 있으면 택시를 탄다 카드마져 없으면 걸어간다.    
# if 'money' in pocket:
#     print("택시를 타고 가자")
# else:
#     if card:
#         print("택시를 타고 가자")
#     else:    
#         print("걸어갑시다")

if 'money' in pocket:
    print("택시를 타고 가자")
elif card:
    print("택시를 타고 가자")
else:
    print("걸어갑시다")
            
        
        