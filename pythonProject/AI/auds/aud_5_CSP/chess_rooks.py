from constraint import *

"""
https://github.com/fcse-is/ai/blob/master/av6/rooks_problem1.py
"""

if __name__ == '__main__':
    # problem = Problem()
    #
    # #variables
    # rooks = range(1,9)
    # #domain
    # domain = range(0,8)
    #
    # problem.addVariables(rooks,domain)
    # # problem.addConstraint(AllDifferentConstraint(), rooks)
    #
    # for rook1 in rooks:
    #     for rook2 in rooks:
    #         if rook1 < rook2:
    #             problem.addConstraint(lambda a,b: a!=b,(rook1, rook2))
    #             # problem.addConstraint(lambda r1,r2: r1[0] != r2[0] and r1[1] != r2[1], (rook1,rook2)) <- za ova na linkot da se vidi
    #
    # solution = problem.getSolution()
    #
    #
    # print(solution)



    def check(r1,r2):
        if r1==r2:
            return False
        return True




    problem = Problem()

    rooks = range(1,9)
    domain = range(0,8)

    problem.addVariables(rooks,domain)

    for r1 in rooks:
        for r2 in rooks:
            if r1 < r2:
                # problem.addConstraint(lambda a,b: a!=b, (r1,r2))
                problem.addConstraint(check, (r1,r2))


    sol = problem.getSolution()

    print(sol)
















