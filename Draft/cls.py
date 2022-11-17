
class Father():
    Name = ""
    # def __init__(cls):
    #     cls.Name = ""
    #     super().__init__()
    @classmethod
    def af(self):
        self.Name = 'Father'

class Son(Father):
    Age = 12
    # def __init__(cls):
    #     super().__init__()
    @classmethod
    def ason(cls):
        cls.Name = 'Son'

    @classmethod
    def aage(cls):
        cls.Age = '14'



class Daughter(Son):
    pass



    def abv(self):
        Son.af()

def assigna(Fa):
    Fa.Name = "Test"


if __name__ == '__main__':
    A = Son()
    Son.Name = "AA"
    d = Son()
    B = Daughter()

    A.ason()
    A.aage()
    print(B.Name,B.Age)
    print(A.Name,A.Age)
        # assigna(Son)
    # d.af()
    B.abv()
    print(B.Name,B.Age)
    print(A.Name,A.Age)
    # print(d.Name)