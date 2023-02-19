"""time delay decorator """
import time

def delay_decorator(function):
    def wrapper_function():
        """code goes here"""
        time.sleep(2)
        function()
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

say_hello()