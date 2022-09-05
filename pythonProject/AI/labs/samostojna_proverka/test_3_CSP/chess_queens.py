from constraint import *

def queens_attacking(q1,q2):
    if q1[0] == q2[0] or \
        q1[1] == q2[1] or \
        abs(q1[0] - q2[0]) == abs(q1[1] - q2[1]): # same column (x) or same row(y) or same diagonal (abs)
        return False
    return True

if __name__ == '__main__':
    # problem = Problem(BacktrackingSolver())
    # variables = ["A", "B", "C", "D", "E", "F","H"]
    number = int(input())

    if number <=6:
        problem = Problem(BacktrackingSolver())
    else:
        problem = Problem()

    variables = range(1,number+1)
    # for variable in variables:
    #     problem.addVariable(variable, Domain(set(range(100))))

    domain = [(i,j) for i in range(number) for j in range(number)]

    problem.addVariables(variables,domain)

    # ---Tuka dodadete gi ogranichuvanjata----------------

    for q1 in variables:
        for q2 in variables:
            if q1 < q2:
                problem.addConstraint(queens_attacking, (q1,q2))

    # ----------------------------------------------------

    if number <=6:
        print(len(problem.getSolutions()))
    else:
        print(problem.getSolution())

