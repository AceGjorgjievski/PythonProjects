
from constraint import *


def not_same_diagonal(q1, q2):
    if abs(q1[0] - q2[0]) == abs(q1[1] - q2[1]):
        return False
    return True

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    num = int(input())

    # variables = ["A", "B", "C", "D", "E", "F"]
    variables = range(1,num+1)
    domain = [(i,j) for i in range(0,num) for j in range(0,num)]
    for variable in variables:
        problem.addVariable(variable, domain)

    # ---Tuka dodadete gi ogranichuvanjata----------------

    problem.addConstraint(AllDifferentConstraint(),variables)

    for queen1 in variables:
        for queen2 in variables:
            if queen1 < queen2 and queen1 != queen2:
                problem.addConstraint(lambda q1, q2: q1 != q2, (queen1, queen2))

                problem.addConstraint(lambda q1, q2: q1[0] != q2[0], (queen1, queen2))
                problem.addConstraint(lambda q1, q2: q1[1] != q2[1], (queen1, queen2))
                problem.addConstraint(lambda q1, q2: (q1[1] - q2[1]) / (q1[0] - q2[0]) != 1, (queen1, queen2))
                problem.addConstraint(lambda q1, q2: (q1[1] - q2[1]) / (q1[0] - q2[0]) != -1, (queen1, queen2))


    # ----------------------------------------------------

    print(problem.getSolution())