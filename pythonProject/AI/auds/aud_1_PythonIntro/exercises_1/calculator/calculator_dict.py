def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


def module(n1, n2):
    return n1 % n2


def integer_division(n1, n2):
    return n1 // n2


def power(n1, n2):
    return n1 ** n2


def multiply(n1, n2):
    return n1 * n2


operators = {
    '+': add,
    '-': sub,
    '/': divide,
    '%': module,
    '//': integer_division,
    '**': power,
    '*': multiply
}

if __name__ == '__main__':
    operand1 = int(input())
    operator = input()
    operand2 = int(input())

    function = operators.get(operator)
    print(f"Rezultatot e {function(operand1, operand2)}")



