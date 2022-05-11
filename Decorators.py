"""Decorators"""


# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         # adding *args, **kwarg accepting as many arguments as needed for the function
#         print(f'wrapper executed this before {original_function.__name__}')
#         return original_function(*args, **kwargs)
#     return wrapper_function
#
#
# @decorator_function
# def display():
#     print('display function ran')
#
#
# # my_display = decorator_function(display)
# # represents same as adding the @decorator_function above the display function
# # instead of typing all the above we only have to type display() and code is executed
# display()
#
#
# # now with multiple decorator functions
# @decorator_function
# def display_info(name: str, age: int):
#     print(f'display_info ran with arguments {name}, {age}')
#
#
# display_info('Tim', 48)
#
#
# # this can also be handled by a decorator class as well
# class DecoratorClass(object):
#
#     def __init__(self, original_function):
#         self.original_function = original_function
#
#     def __call__(self, *args, **kwargs):
#         print(f'call method executed this before {self.original_function.__name__}')
#         return self.original_function(*args, **kwargs)
#
#
# @DecoratorClass
# def display():
#     print('display function ran')
#
#
# @DecoratorClass
# def display_info(name: str, age: int):
#     print(f'display_info ran with arguments {name}, {age}')
#
#
# display()
# display_info('Julia', 42)


# practical example
from functools import wraps     # is needed when running decorators on top of eachother
import time


def my_logger(original_function):
    """Function to log arguments used when executing a specific function, and keep track of it in a log file"""
    import logging
    logging.basicConfig(filename=f'{original_function.__name__}.log', level=logging.INFO)

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        logging.info(f'Ran with args:{args}, and kwargs:{kwargs}')
        return original_function(*args, **kwargs)
    return wrapper


def my_timer(original_function):
    """Function to check how long it takes to run a specific function."""
    import time

    @wraps(original_function)
    def wrapper(*arg, **kwargs):
        t1 = time.time()
        result = original_function(*arg, **kwargs)
        t2 = time.time() - t1
        print(f'{original_function.__name__} ran in:{t2} sec.')
        return result
    return wrapper


@my_logger
@my_timer
def display_info(name: str, age: int):
    time.sleep(1)
    print(f'display_info ran with arguments {name}, {age}')


display_info('Tom', 20)
