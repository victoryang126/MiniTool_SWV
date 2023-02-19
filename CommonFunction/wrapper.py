import functools
import traceback
def func_monitor(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        # print('args = {}'.format(*args))
        ret = None
        try :
            # ret = func(*args, **kwargs)
            # print('finished  %s():' % func.__name__)
            return func(*args, **kwargs)
        except Exception as e:
            # pass
            # analyze_exception(e)
            print(traceback.format_exc())
            # raise e
        # return ret

    return wrapper

a = [1,2]
@func_monitor
def p(a):
    print(a[3])
p(a)