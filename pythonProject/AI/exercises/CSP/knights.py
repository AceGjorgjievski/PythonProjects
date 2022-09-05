from constraint import *


def check_attacking(k1, k2):
    return not (abs(k1[0] - k2[0]) == abs(k1[1] - k2[1]))

if __name__ == '__main__':
    problem = Problem()

    variables = range(1, 9)

    domain = [(i, j) for i in range(8) for j in range(8)]

    problem.addVariables(variables,domain)

    for knight1 in variables:
        for knight2 in variables:
            if knight1 < knight2:
                problem.addConstraint(check_attacking, (knight1, knight2))

    print(problem.getSolution())


