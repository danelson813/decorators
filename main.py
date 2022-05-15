from app import decorator


@decorator
def add(num1, num2):
    return num1 + num2


print(add(7, 4))