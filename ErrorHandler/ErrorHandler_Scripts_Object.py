from ImportModule import *
@dataclass
class TSStep_Flag:
    start_log:bool=True
    stop_log:bool = True
    step:bool = True
    flag:str = None

@dataclass
class TSStep:
    step:int = 0
    sub_step:int = 0
    deepth:int = 1

    def tabs(self):
        return "\t"*self.deepth

class Func_Policy:
    FUNC = "FUNC"
    NORMAL = "NORMAL"
    TIMER = "TIMER"
    DTC = "DTC"