


가로 = 0
세로 = 0

def __init__(self):
    self.가로
    self.세로

def 가로세로(self,가로,세로):

    가로 = int(input("사각형의 가로를 입력해주세요"))
    세로 = int(input("사각형의 세로를 입력해주세요"))
    사각형넓이 = 가로 * 세로
    print("-" * 10)
    print("사각형의 넓이" + (str(사각형넓이)))

def 둘레둘레(self,가로,세로):

    가로 = int(input("사각형의 가로를 입력해주세요"))
    세로 = int(input("사각형의 세로를 입력해주세요"))
    사각형둘레 = (가로 + 세로) *2
    print("-" * 10)
    print("사각형의 둘레" + (str(사각형둘레)))

가로세로(가로세로,가로,세로)
둘레둘레(둘레둘레,가로,세로)