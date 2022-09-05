from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = []
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(100))))

    # ---Tuka dodadete gi ogranichuvanjata----------------

    # ----------------------------------------------------

    print(problem.getSolution())