from constraint import *

if __name__ == '__main__':
    # solver = input()

    problem = Problem()
    variables = range(0, 81)
    domain = range(1,10)

    for variable in variables:
        problem.addVariable(variable, domain)



    # ---Tuka dodadete gi ogranichuvanjata----------------

    problem.addConstraint(AllDifferentConstraint(), variables)


    for i in range(9):
        problem.addConstraint(ExactSumConstraint(45), [row*9 + i for row in range(9)])

    for j in range(9):
        problem.addConstraint(ExactSumConstraint(45), [j + row*9 for row in range(9)])



    # ----------------------------------------------------

    print(problem.getSolution())