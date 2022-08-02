# 클래스변수
class Temp:
    tmp = 100  # 클래스 변수(모든 객체의 클래스 변수는 같은 메모리를 사용)
    

#객체
t1 = Temp()
t2 = Temp()
t3 = Temp()
print(f"t1 tmp : {t1.tmp}  t2 tmp : {t2.tmp} t3 tmp : {t3.tmp}")
# t1 tmp : 100  t2 tmp : 100 t3 tmp : 100

t1.tmp = 200 # 인스턴스 변수(객체변수)    가 생성됨
print(f"t1 tmp : {t1.tmp}  t2 tmp : {t2.tmp} t3 tmp : {t3.tmp}")
# t1 tmp : 200  t2 tmp : 100 t3 tmp : 100
#클래스변수
Temp.tmp = 500
print(f"t1 tmp : {t1.tmp}  t2 tmp : {t2.tmp} t3 tmp : {t3.tmp}")
# t1 tmp : 200  t2 tmp : 500 t3 tmp : 500    