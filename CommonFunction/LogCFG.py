import logging
import colorlog
from logging.handlers import RotatingFileHandler
import traceback
import functools

color_config = {
    'DEBUG': 'black',
    'INFO': 'black',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'red',
}
console_fmt = '%(log_color)s%(asctime)s--%(levelname)s--%(filename)s  %(pathname)s %(module)s  %(funcName)s -[line:%(lineno)d]-s : %(message)s'
func_console_fmt ='%(log_color)s%(asctime)s--%(levelname)s--%(filename)s  %(module)s  %(funcName)s -[line:%(lineno)d]-s : %(message)s'
file_fmt = '%(asctime)s-%(levelname)s-%(filename)s  %(pathname)s %(module)s  %(funcName)s -[line:%(lineno)d]-s : %(message)s'


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
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        Monitor_Logger.info('call %s():' % func.__name__)
        Debug_Logger.debug('call %s():' % func.__name__)
        # print('args = {}'.format(*args))
        ret = None
        ret = func(*args, **kwargs)
        Monitor_Logger.info('finished %s():' % func.__name__)
        Debug_Logger.debug('finished %s():' % func.__name__)
        return ret
    return wrapper

def analyze_exception():
    Exception_Logger.critical(traceback.format_exc())

@func_monitor
def p_with_monitor(lis):
    try:
        print(lis[3])
    except Exception as e:
        analyze_exception()
if __name__ == '__main__':
    # 控制台只会显示warning及以上级别日志信息，而log.txt文件中则会记录error及以上级别日志信息

    a = [1, 2]

    p_with_monitor(a)
