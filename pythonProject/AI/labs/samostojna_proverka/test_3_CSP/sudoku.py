from constraint import *


"""
https://prnt.sc/tv8sDgtkY5tS

input:
BacktrackingSolver
output:
{0: 9, 1: 8, 2: 7, 3: 6, 4: 5, 5: 4, 6: 3, 7: 2, 8: 1, 9: 6, 10: 5, 11: 4, 15: 9, 16: 8, 17: 7, 12: 3, 13: 2, 14: 1, 18: 3, 19: 2, 20: 1, 21: 9, 22: 8, 23: 7, 24: 6, 25: 5, 26: 4, 27: 8, 29: 9, 32: 6, 35: 5, 28: 7, 30: 4, 31: 3, 34: 1, 33: 2, 40: 9, 49: 7, 51: 8, 42: 7, 44: 6, 43: 4, 37: 3, 38: 5, 36: 2, 41: 8, 39: 1, 47: 6, 45: 4, 46: 1, 48: 5, 50: 2, 52: 9, 53: 3, 54: 7, 57: 8, 56: 3, 61: 6, 55: 9, 59: 5, 62: 2, 58: 4, 60: 1, 63: 5, 69: 4, 64: 6, 67: 1, 72: 1, 73: 4, 76: 6, 78: 5, 65: 8, 71: 9, 68: 3, 70: 7, 66: 2, 74: 2, 75: 7, 77: 9, 79: 3, 80: 8}


"""



def check_constrain(num1,num2):
    if num1[0] == num2[0] or num1[1] == num2[1]:
        return False
    return True

def solve(variables, domain, problem):
    for row in range(0,9):
        problem.addConstraint(AllDifferentConstraint(),[row * 9 + i for i in range(1,10)])

    for col in range(0,9):
        problem.addConstraint(AllDifferentConstraint(), [col + 9*i for i in range(1,10)])




if __name__ == '__main__':

    # solver = input()
    # solver = solver + '()'
    problem = Problem(BacktrackingSolver())
    variables = range(0,81)
    domain = range(1,10)
    # for variable in variables:
    #     problem.addVariable(variable, Domain(set(range(100))))

    solve(variables,domain,problem)

    problem.addVariables(variables,domain)
    # ---Tuka dodadete gi ogranichuvanjata----------------

    for num1 in variables:
        for num2 in variables:
            if num1 < num2:
                # problem.addConstraint(lambda a,b: a!=b, (num1,num2))
                problem.addConstraint(check_constrain, (num1,num2))

    # ----------------------------------------------------

    print(problem.getSolution())