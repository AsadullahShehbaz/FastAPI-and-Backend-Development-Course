# Lecture 3.2 - Decorators from scratch
from typing import Any, Callable


# 1) Simplest decorator: wraps a function, must RETURN the wrapper
def fence(f):
    def wrapper():
        print("+" * 10)
        f()
        print("+" * 10)
    return wrapper


@fence
def log():
    print("decorated")


log()


# 2) Decorator that takes its own argument -> one extra wrapping level
def custom_fence(symbol: str = "+"):
    def decorator(f):
        def wrapper(text: str):
            print(symbol * len(text))
            f(text)
            print(symbol * len(text))
        return wrapper
    return decorator


@custom_fence("-")
def show(text: str):
    print(text)


show("Wireless Mouse")

# 3) Typing a function argument
add: Callable[[int, int], int | float]
anything: Callable[[Any], Any]
