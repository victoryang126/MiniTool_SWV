import re

class RegCompare:
    def __init__(self):
        pass

    def is_digital_str(self,value):
        return re.match("^\d+$",value)

    def is_equal(self,a:str,b:str):
        pattern = "^" + a +"$"
        return re.match(pattern,b,re.I)


regCompare = RegCompare()
if __name__ == "__main__":
    print(regCompare.is_equal('a',"A"))
