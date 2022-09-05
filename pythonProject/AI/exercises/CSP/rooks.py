from constraint import *

# (i1, j1), (i2, j2)
def different(rook1,rook2):
    return rook1[0] != rook2[0] and rook1[1] != rook2[1]

if __name__ == '__main__':
    problem = Problem()

    rooks = range(1, 9)
    domain = []
    for i in range(0, 8):
        domain.append(i)

    # print(domain)

    problem.addVariables(rooks, domain)

    for rook1 in rooks:
        # for rook2 in range(rook1+1,len(rooks)): another way i think
        for rook2 in rooks:
            if rook1 < rook2:
                # problem.addConstraint(different, (rook1, rook2))
                problem.addConstraint(lambda r1,r2: r1!=r2, (rook1,rook2))

    print(problem.getSolution())
    #{1: 7, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1, 8: 0}


