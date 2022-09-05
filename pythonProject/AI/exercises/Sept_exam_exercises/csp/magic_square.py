from constraint import *

if __name__ == '__main__':
    problem = Problem()

    variables = range(0, 16)
    domain = range(1, 17)

    problem.addVariables(variables, domain)

    """
    0  1  2  3
    4  5  6  7
    8  9 10 11
   12 13 14 15
    """

    problem.addConstraint(AllDifferentConstraint(),variables)

    problem.addConstraint(ExactSumConstraint(34), range(0, 16, 5))  # main diagonal
    problem.addConstraint(ExactSumConstraint(34), range(3, 13, 3))  # opposite diagonal

    for row in range(0, 4):
        problem.addConstraint(ExactSumConstraint(34), [row * 4 + i for i in range(0, 4)])

    for col in range(0, 4):
        problem.addConstraint(ExactSumConstraint(34), [col + 4 * i for i in range(0, 4)])

    print(problem.getSolution())
