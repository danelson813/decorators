from functools import wraps


def decorator(func):
    print('in decorator')

    @wraps(func)
    def wrapper(*args, **kwargs):
        print('in wrapper.')
        print('Do something before the function executes.')

        value = func(*args, **kwargs)

        print('inside wrapper.')
        print("Do something after the function is executed")

        return value

    return wrapper


@decorator
def func2():
    print('inside func2')
    print("now is the time.")


@decorator
def multi_10(number: int, times=1):
    print('inside the original function')
    return number * 10 ** times


if __name__ == '__main__':
    pass
