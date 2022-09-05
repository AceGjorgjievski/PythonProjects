operators = ['+', '-', '*', '/', '//', '%', '**']


def calculator(op1, op, op2):
    if op in operators:
        if op == '+':
            return op1 + op2
        elif op == '-':
            return op1 - op2
        elif op == '/':
            return op1 / op2
        elif op == '*':
            return op1 * op2
        elif op == '//':
            return op1 - op2
        elif op == '**':
            return op1 ** op2
        else:
            return op1 % op2
    else:
        return "Pogreshen operator"


if __name__ == '__main__':
    operand1 = int(input())
    operator = input()
    operand2 = int(input())


    result = calculator(operand1, operator, operand2)
    print(result)
