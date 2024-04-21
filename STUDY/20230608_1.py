import math
#

class 은행():
    def __init__(self, a, b, c):
        a += b - c
        self.현잔고 = a
        self.입금액 = b
        self.출금액 = c
        print(a)

은행(10000, 5000, 8000)

class 상속(은행):
    def 루트값(self):
        super.__init__
        ge = math.sqrt(self.현잔고)
        print(ge)
        return ge
        
    def 잘못된계산기능(self):
        a = 상속.루트값(self)
        a1 = (int(input("a에 몇을 곱하시겠습니까? >>")))
        #b = math.sqrt(int(input("b 하시겠습니까? >>")))
        #c = math.sqrt(int(input("c 하시겠습니까? >>")))
        print(int(a * a1))
        
#상속.__init__(상속, 10000, 5000, 8000)
상속.__init__(상속, 10000, 5000, 8000)
#상속.루트값(상속)
상속.잘못된계산기능(상속)

