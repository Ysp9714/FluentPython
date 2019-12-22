from time import time

def get_time(func):
    def decorate(*args, **kwargs):
        now = time()
        func_return = func(*args, **kwargs)
        print(time() - now)
    return decorate
    

