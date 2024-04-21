class Employee:
    name = None
    pay = 0

    def __init__(self,name):
        self.name = name

class 정규직(Employee):
    pass

class 계약직(Employee):
    pass
