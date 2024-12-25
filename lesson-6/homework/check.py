def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)
    return wrapper

@check
def div(a, b):
    return a / b

a = int(input('Enter a: '))
b = int(input('Enter b: '))
print(div(a, b))