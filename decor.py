"""
def decorator_func(original_func):
    def wrapper_func(*args,**kwargs):
        print(f"wrapper func ran before {original_func.__name__}")
        return original_func(*args,**kwargs)
    return wrapper_func


@decorator_func
def display():
    print("Display function ran")

@decorator_func
def display_info(name,age):
    print(f'display_info ran with arguments {name}, {age}')


display_info('Edwin',69)




class decorator_class(object):
    def __init__(self,original_func):
        self.original_func = original_func
    
    def __call__(self,*args,**kwargs):
        print('this ran before original func')
        return self.original_func(*args,**kwargs)

@decorator_class
def display():
    print("Display function ran")


@decorator_class
def display_info(name,age):
    print(f'dislay_info ran with arguments {name} and {age}.')
"""
from functools import wraps
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=f'{orig_func.__name__}.log', level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args,**kwargs):
        logging.info(
            f'{orig_func.__name__} ran with args: {args} and kwargs: {kwargs}'
        )
        return orig_func(*args,**kwargs)
    return wrapper

def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args,**kwargs):
        t1 = time.time()
        result = orig_func(*args,**kwargs)
        t2 = (time.time() - t1)
        print(f'{orig_func.__name__} ran in {t2}')
        return result
    return wrapper

  


import time 

@my_timer
@my_logger
def display_info(name,age):
    time.sleep(1)
    print(f'dislay_info ran with arguments {name} and {age}.') 


display_info('Edwin',21)