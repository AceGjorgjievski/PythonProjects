from constraint import *

"""
https://prnt.sc/mSOWmuKQnt0Y <<< ima greshka pri presmetka x1[0] - x2[0], x1[1] - x2[1]

slika ^^^

"""

def knigts_attacking(kn1, kn2): # ova vazhi samo za konji da ne se napagjaat i pritoa da ne se na ista redica/kolona
    if abs(kn1[0]-kn2[0]) == (kn1[1]-kn2[1]):
        return False
    return True



if __name__ == '__main__':
    problem = Problem()

    domain = [(i,j) for i in range(8) for j in range(8)]

    #No. od Knigts
    variables = range(1,9) #1...8

    problem.addVariables(variables,domain)

    for kn1 in variables:
        for kn2 in variables:
            if kn1 < kn2:
                problem.addConstraint(knigts_attacking,(kn1,kn2))

    solution = problem.getSolution()

    print(solution)







