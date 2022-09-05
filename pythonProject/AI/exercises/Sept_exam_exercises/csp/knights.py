from constraint import *

"""

"""

def knights_attacking(k1, k2):
    ...

if __name__ == '__main__':
    problem = Problem()

    variables = range(0, 8)
    domain = [(i,j) for i in range(0, 8) for j in range(0, 8)]

    problem.addVariables(variables, domain)

    for k1 in variables:
        for k2 in variables:
            if k1 < k2:
                problem.addConstraint(knights_attacking, (k1, k2))


    print(problem.getSolution())




