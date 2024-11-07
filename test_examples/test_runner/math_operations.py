def add(a, b):
    try:
        return a + b
    except TypeError as e:
        return e


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    if b == 0:
        raise ValueError("Cannot power of zero")
    return a ** b
