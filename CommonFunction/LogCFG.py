import logging
import colorlog
from logging.handlers import RotatingFileHandler
import traceback
import functools
import os

if os.path.exists("logs") and os.path.isdir("logs"):
    pass
else:
    os.makedirs("logs")

color_config = {
    'DEBUG': 'black',
    'INFO': 'black',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'red',
}
console_fmt = '%(log_color)s%(asctime)s ---%(levelname)s--- %(filename)s  %(pathname)s %(module)s  %(funcName)s -[line:%(lineno)d]-s : %(message)s'
func_console_fmt ='%(log_color)s%(asctime)s ---%(levelname)s--- %(filename)s  %(module)s  %(funcName)s -[line:%(lineno)d]-s : %(message)s'
file_fmt = '%(asctime)s ---%(levelname)s--- %(filename)s  %(pathname)s %(module)s  %(funcName)s -[line:%(lineno)d]-s : %(message)s'


console_formatter = colorlog.ColoredFormatter(fmt=console_fmt, log_colors=color_config)
func_console_formatter = colorlog.ColoredFormatter(fmt=func_console_fmt, log_colors=color_config)

file_formatter = logging.Formatter(fmt=file_fmt)

ExceptionFile = "logs\MiniTool_Exception.log"
DebugFile = "logs\MiniTool_Debug.log"

Exception_Logger = logging.getLogger("__EXCEPTION__")
# 指定最低日志级别：（critical > error > warning > info > debug）
Exception_Logger.setLevel(logging.CRITICAL)
Debug_Logger = logging.getLogger("__DEBUG__")
Debug_Logger.setLevel(logging.DEBUG)
Monitor_Logger = logging.getLogger( "__MONITOR__")
Monitor_Logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
func_console_handler = logging.StreamHandler()
Exception_file_handler = logging.FileHandler(filename=ExceptionFile, mode="a", encoding='utf-8')
Debug_file_handler = logging.FileHandler(filename=DebugFile, mode="a", encoding='utf-8')

console_handler.setFormatter(console_formatter)
func_console_handler.setFormatter(func_console_formatter)
Exception_file_handler.setFormatter(file_formatter)
Debug_file_handler.setFormatter(file_formatter)

Exception_Logger.addHandler(Exception_file_handler)
Exception_Logger.addHandler(console_handler)

Monitor_Logger.addHandler(func_console_handler)

Debug_Logger.addHandler(Debug_file_handler)


def clear_log():
    with open(ExceptionFile, "w"):
        pass
    with open(DebugFile, "w"):
        pass



def func_monitor(func):
    # Monitor_Logger.info('call %s():' % func.__name__)
    # Debug_Logger.debug('call %s():' % func.__name__)
    # Monitor_Logger.info(f"{func.__name__} args = {func.__code__.co_varnames}")
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        Monitor_Logger.info(f"CALL FUNCTION: {func.__name__}")
        Debug_Logger.debug(f"CALL FUNCTION: {func.__name__}")
        Debug_Logger.debug(f'args = {args}')
        Debug_Logger.debug(f'kwargs = {kwargs}')
        ret = None
        ret = func(*args, **kwargs)
        Monitor_Logger.info(f"EXECUTE FUNCTION {func.__name__} SUCCESSFULLY")
        Debug_Logger.debug(f"FUNCTION {func.__name__} RETURN VALUE\n: {ret}")
        Debug_Logger.debug(f"EXECUTE FUNCTION {func.__name__} SUCCESSFULLY")
        return ret
    return wrapper

def analyze_exception():
    Exception_Logger.critical(traceback.format_exc())
#
@func_monitor
def p_with_monitor(lis,c,d,e):
    try:
        print(lis[4])
        # Monitor_Logger.info('finished %s():' % fun_name)
    except Exception as err:
        # Exception_Logger.critical(traceback.format_exc())
        analyze_exception()
    return lis,c,d,e
if __name__ == '__main__':
    pass
    # # 控制台只会显示warning及以上级别日志信息，而log.txt文件中则会记录error及以上级别日志信息
    # # attrs = dir(p_with_monitor)
    #
    # # print(p_with_monitor.__code__.co_cellvars)
    # # print(p_with_monitor.__code__.co_consts)
    # # for attr in attrs:
    # #     print(attr)
    # #     # print(p_with_monitor.attr)
    # #     print(getattr(p_with_monitor, attr))
    a = [1, 2]
    c = "3"
    d = 5
    e = {"a":1,"b":2}
    p_with_monitor(*[a,c],d =d,e=e)
    # print(dir(p_with_monitor))

