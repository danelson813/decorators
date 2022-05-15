# def decorator(func):
#     print("in decorator")
#
#     def wrapper():
#         print("Inside wrapper")
#         print("Do something before function")
#         value = func()
#         print("Inside wrapper")
#         print("Do something after function")
#         return value
#     return wrapper
#
#
# @decorator
# def func2():
#     print("Inside func2")


# func2()


def decorator2(func):
    print("Inside decorator")

    def wrapper(*args, **kwargs):
        print("Inside wrapper.")
        print("Do something before the function.")
        value = func(*args, **kwargs)
        print("Inside wrapper")
        print("Do something after the function")
        return value
    return wrapper


@decorator2
def multi_10(number: int, times: int=1):
    print("Inside original function")
    return number * 10 ** times


print(multi_10(1, times=3))
