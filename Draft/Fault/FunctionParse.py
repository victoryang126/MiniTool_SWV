"""
1. 在某个配置文件里面传入函数，例如CheckDCSStatusByDID(Test_Object_Str,Buckled)

2. 然后通过python 对象添加方法到python对象中

3. 最后根据Excel

"""

def CallFunction2Ts(EventName,*args,ScriptFile):
    CallAction = EventName + "(" + ",".join(args)  + ")"



if __name__ == "__main__":
    pass