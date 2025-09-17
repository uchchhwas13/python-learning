import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start}")
        return result
    return wrapper


@timer
def example_function(n):
    time.sleep(n)


def debug(func):
    def wrapper(*args, **kwargs):
        args_values = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        print(
            f"calling: {func.__name__} with args {args_values} and kwargs {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper


@debug
def hello():
    print("hello")


@debug
def greet(name, greeting="hello"):
    print(f"{greeting}, {name}")


hello()
greet("john", greeting="Hi")
# example_function(2)
