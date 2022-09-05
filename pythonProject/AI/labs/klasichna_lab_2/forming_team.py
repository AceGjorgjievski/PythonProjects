from constraint import *


# given:
# https://prnt.sc/b8M8-S7ZMp_0


#test cases:
# https://prnt.sc/QK6cuxO7iZTX

# https://prnt.sc/NBT5F-YUrPUA

maxSum = 0.0
problem = Problem()

def check_valid(clen1, clen2, clen3, clen4, clen5, lider):
    # print(clen1)
    # print(clen2)
    # print(clen3)
    # print(clen4)
    # print(clen5)
    #
    # print(lider)

    currSum = clen1 + clen2 + clen3 + clen4 + clen5 + lider

    problem.addConstraint(InSetConstraint(), (currSum))
    return True

    # global maxSum
    # if currSum <= 100 and currSum > maxSum:
    #     maxSum = currSum
    #     print(clen1)
    #     print(clen2)
    #     print(clen3)
    #     print(clen4)
    #     print(clen5)
    #
    #     print(lider)
    #     print("===============================================================")
    #     return True

    # return False

    # print(type(clen1))
    # print(type(lider))



if __name__ == '__main__':


    clenovi_variables = []
    clenovi_tezhina = []

    lideri_variables = []
    lideri_tezhina = []

    broj_clenovi = int(input())

    for i in range(broj_clenovi):
        par = str(input()).split(" ")
        tezhina = float(par[0])
        clenovi_tezhina.append(tezhina)
        clenovi_variables.append(par[1])
        problem.addVariable(par[1], [tezhina])

    broj_lideri = int(input())

    for i in range(broj_lideri):
        par = input().split(" ")
        tezhina = float(par[0])
        lideri_tezhina.append(tezhina)
        lideri_variables.append(par[1])
        problem.addVariable(par[1], [tezhina])

    variables_all = []
    for i in range(broj_clenovi):
        variables_all.append(clenovi_variables[i])

    for i in range(broj_lideri):
        variables_all.append(lideri_variables[i])

    problem.addConstraint(AllDifferentConstraint(), variables_all)

    # for i in range(len(clenovi_variables)):
    #     for j in range(i + 1, len(clenovi_variables)):
    #         for k in range(j + 1, len(clenovi_variables)):
    #             for m in range(k + 1, len(clenovi_variables)):
    #                 for n in range(m + 1, len(clenovi_variables)):
    #                     for o in range(len(lideri_variables)):
    #                         problem.addConstraint(check_valid, (clenovi_variables[i],
    #                                                             clenovi_variables[j],
    #                                                             clenovi_variables[k],
    #                                                             clenovi_variables[m],
    #                                                             clenovi_variables[n],
    #                                                             lideri_variables[o]))
    #                         # problem.addConstraint(MaxSumConstraint(100), (clenovi_variables[i],
    #                         #                                     clenovi_variables[j],
    #                         #                                     clenovi_variables[k],
    #                         #                                     clenovi_variables[m],
    #                         #                                     clenovi_variables[n],
    #                         #                                     lideri_variables[o]))

    maxSum = 0.0
    finalMaxSum = 0.0
    def check_valid2(clen1, clen2, clen3, clen4, clen5, lider):
        # print(type(clen1))
        # print(type(lider))
        # print("==============")
        if (clen1 + clen2 + clen3 + clen4 + clen5 + lider) <= 100:
            return (clen1 + clen2 + clen3 + clen4 + clen5 + lider)
        return None

    finalClen1, finalClen2, finalClen3, finalClen4, finalClen5, finalLider = None, None, None, None, None, None

    for i in range(len(clenovi_variables)):
        for j in range(i + 1, len(clenovi_variables)):
            for k in range(j + 1, len(clenovi_variables)):
                for m in range(k + 1, len(clenovi_variables)):
                    for n in range(m + 1, len(clenovi_variables)):
                        for o in range(len(lideri_variables)):
                            local = check_valid2(clenovi_tezhina[i],
                                         clenovi_tezhina[j],
                                         clenovi_tezhina[k],
                                         clenovi_tezhina[m],
                                         clenovi_tezhina[n],
                                         lideri_tezhina[o])
                            if  local != None and local >= maxSum:
                                finalClen1 = clenovi_variables[i]
                                finalClen2 = clenovi_variables[j]
                                finalClen3 = clenovi_variables[k]
                                finalClen4 = clenovi_variables[m]
                                finalClen5 = clenovi_variables[n]
                                finalLider = lideri_variables[o]
                                maxSum = local



    # print(problem.getSolution())


    """
Participant 1: Y
Participant 2: X
Participant 3: V
Participant 4: T
Participant 5: R

Participant 1: R
Participant 2: T
Participant 3: V
Participant 4: X
Participant 5: Y
    
    """


    print(f"Total score: {round(maxSum,1)}")
    print(f"Team leader: {finalLider}")

    print(f"Participant 1: {finalClen5}")
    print(f"Participant 2: {finalClen4}")
    print(f"Participant 3: {finalClen3}")
    print(f"Participant 4: {finalClen2}")
    print(f"Participant 5: {finalClen1}")

