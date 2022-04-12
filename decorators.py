import functools

import functools

def debug(func):
    """Выводит сигнатуру функции и возвращаемое значение"""
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Вызываем {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} вернула значение - {value!r}")
        return value
    return wrapper_debug

