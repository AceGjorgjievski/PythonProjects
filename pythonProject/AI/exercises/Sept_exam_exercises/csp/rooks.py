from constraint import *

def not_attacking(r1,r2):
    return r1[0] != r2[0] and r1[1] != r2[1]

if __name__ == '__main__':
    problem = Problem()

    # rooks = range(0, 8)
    # domain = [(i, j) for i in range(0, 8) for j in range(0, 8)]
    #
    # problem.addVariables(rooks, domain)
    #
    # for rook1 in rooks:
    #     for rook2 in rooks:
    #         if rook1 < rook2:
    #             problem.addConstraint(lambda a,b: a[0] != b[0] and a[1] != b[1], (rook1,rook2))
    #
    # result = problem.getSolution()
    # print(result)

    # rooks = range(0, 8) # row
    # domain = range(0, 8)
    #
    # problem.addVariables(rooks, domain)
    #
    # for rook1 in rooks:
    #     for rook2 in rooks:
    #         if rook1 < rook2:
    #             problem.addConstraint(lambda a,b: a!=b, (rook1, rook2))
    #
    # print(problem.getSolution())


    rooks = range(0,8)
    domain = range(0,8)

    problem.addVariables(rooks, domain)

    problem.addConstraint(AllDifferentConstraint(), rooks)
    print(problem.getSolution())




