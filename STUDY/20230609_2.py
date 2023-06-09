class 사람():
    이름 = None
    성별 = None
    나이 = None
    
    def __init__(self,이름,성별,나이):
        self.이름 = 이름
        self.성별 = 성별
        self.나이 = 나이
    
    def 화면(self):
        self.이름 = str(input("이름 입력 : "))
        self.성별 = str(input("성별 입력 : "))
        self.나이 = str(input("나이 입력 : "))
        print("=" * 10)

        print("이름 : ", self.이름)
        print("성별 : ", self.성별)
        print("나이 : ", self.나이)
        

# b3 = i('하양이','10000')
p = 사람(사람.이름,사람.성별,사람.나이)
사람.화면(사람)