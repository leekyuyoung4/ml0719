PI = 3.141592

class CalcCircle:
    def calc(self, r):
        return PI*(r**2)

def add(a,b):
    result = 0
    for i in range(b):
        result += a;
    return result