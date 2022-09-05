from constraint import *





if __name__ == '__main__':
    problem = Problem()


    variables = range(0,16) #0...16

    domain = range(1,17) #1...16

    problem.addVariables(variables,domain)

    problem.addConstraint(AllDifferentConstraint(),variables)# na sekoe pole da imame razlichen broj

    """
    0  1   2   3
    4  5   6   7
    8  9  10  11
    12 13 14  15
    
    """

    for row in range(4):
        problem.addConstraint(ExactSumConstraint(34),[4*row+i for i in range(0,4)])

    for col in range(4):
        problem.addConstraint(ExactSumConstraint(34),[col+4*i for i in range(0,4)])


    problem.addConstraint(ExactSumConstraint(34),range(0,16,5))
    problem.addConstraint(ExactSumConstraint(34),range(3,13,3))

    solution = problem.getSolution()
    print(solution)





