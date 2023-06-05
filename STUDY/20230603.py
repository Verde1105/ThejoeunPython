class BlackBOX:
    pass
b1 = BlackBOX()
b1.name = '까망이'
print(b1.name)

class pan:
    def __init__(self,name,price) :
        self.이름 = name
        self.값 = price
    def set_여행_(self,min):
        print(str(min)+'분 동안 지속')
b2 = pan('하양이','10000')
print(b2.값,b2.이름)
b2.set_여행_(20)

class i(pan):
    # 생성자 : 인스턴스 생성, 호출(X)
    # def __init__(self,name,price) :
    #     self.이름 = name
    #     self.값 = price

    def set_여행_(self,min):
        print(str(min)+'분 동안 지속')
    def set_san_(self,san):
        print(str(san)+'개')

# b3 : 인스턴스 
# i('하양이','10000') : 생성자
# b3 = i('하양이','10000')
i.set_san_(i,20)


#슈퍼
class a(pan):
    def __init__(self,name,price,sd) :
        pan.__init__(self,name,price)
        self.sd = sd
        #방법이 두가지
        #부모클래스이름.메소드명(인스턴스생성조건들-self,name 등등)
        #super().메소드명(이렇게 부르면 셀프는 필요없어짐.)


