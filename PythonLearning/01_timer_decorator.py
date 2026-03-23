
# Import Libraries
import time

def timer(fun):
    """
        Decorator Function
        Problem Statement: Timing function execution
    """
    def wrapper(*args, **kwargs):
        start =  time.time()
        result = fun(*args, **kwargs)
        end = time.time()
        print(f"{fun.__name__} ran in: {end - start}")
        return result
    return wrapper

def debug(func):
    """
        Decorator Function
        Problem Statement: Create decorator to print function name and values of its arguements every time the function is called.  
    """
    def wrapper(*args, **kwargs):
        args_value = " ,".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{key} = {value}" for key, value in kwargs.items())
        print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        result = func(*args, **kwargs)
        return result
    return wrapper 

def cache(func):
    """
        Decorator Function
        Problem Statement: Implement a decorator function that caches the return value of function so, that when it's called with the same argurements, the cached value is returned instead of re-executing the function.
    """ 
    cache_value = {}
    print(cache_value)
    def wrapper(*args, **kwargs):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

def example_func(num):
    """
    Docstring for example_funcS
    :param num: integer value for time
    """
    time.sleep(num)

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")
@cache
def long_run_function(a, b):
    time.sleep(4)
    return a + b

# Function calling
# example_func(2)
# greet("Suman Rautela", greeting="Hello")

print(long_run_function(2, 3))
print(long_run_function(2, 3))
print(long_run_function(2, 6))