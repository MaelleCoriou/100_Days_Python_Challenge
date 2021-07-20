def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def devide(n1, n2):
    return n1 / n2


def substract(n1, n2):
    return n1 - n2


def calculator(n1, n2, func):
    return func(n1, n2)


# call func without parenthesis
result = calculator(5, 4, multiply)
print(result)

result = calculator(5, 4, substract)
print(result)
