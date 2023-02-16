from constraint import *

if __name__ == '__main__':
    variables = range(0, 16)
    domain = range(1, 17)

    problem = Problem()
    problem.addVariables(variables, domain)

    """
     0   1  2  3
     4   5  6  7
     8   9 10 11
     12 13 14 15
     
     {0: 16, 3: 16, 5: 16, 10: 1, 
     15: 1, 6: 16, 9: 1, 12: 1, 
     1: 1, 2: 1, 4: 1, 7: 1, 
     8: 16, 11: 16, 13: 16, 14: 16}
    """

    # problem.addConstraint(AllDifferentConstraint(), variables)

    for i in range(4):
        problem.addConstraint(ExactSumConstraint(34), [4 * i + row for row in range(4)])

    for j in range(4):
        problem.addConstraint(ExactSumConstraint(34), [4 * row + j for row in range(4)])

    problem.addConstraint(ExactSumConstraint(34), range(0,16,5))
    problem.addConstraint(ExactSumConstraint(34), range(3,13,3))

    result = problem.getSolution()
    print(result)
