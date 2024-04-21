class MyClass:
    def __init__(self):
        self._my_variable = 0  # 변수 앞에 _를 붙이면 밖에서 못불러온다고 들음.

    def get_my_variable(self):
        return self._my_variable
    
my_object = MyClass() #생성자 () 호출하여, 인스턴스 my_object 생성
value = my_object.get_my_variable() #값 = 인스턴스명.메소드명()
print(value)  # 출력: 

#위는 예시

class 뱅크예시:
    #앞에 _ 를 두개 붙이면 은닉되어, 밖에서 불러올수가 없음. 자바의 프라이빗같은것.
    __잔액 = 0
    __예금주 = None
    __계좌 = None
    
    def __init__(self, 잔액, 이름, 계좌):
        pass
