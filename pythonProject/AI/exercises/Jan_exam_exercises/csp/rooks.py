from constraint import *


def not_attacking(r1, r2):
    return r1 != r2


if __name__ == '__main__':
    # domain = [(i,j) for i in range(0,8) for j in range (0,8)]
    domain2 = range(0, 8)  # rows
    # columns
    rooks = range(1, 9)

    problem = Problem()
    problem.addVariables(rooks, domain2)

    # ne dozvoluvame vrednosta na domain-ot shto go
    # imaat otpovite da bide ista
    for r1 in rooks:
        for r2 in rooks:
            if r1 < r2:
                problem.addConstraint(not_attacking, (r1, r2))

    result = problem.getSolution()

    print(result)
