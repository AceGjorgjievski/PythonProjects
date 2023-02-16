from constraint import *

# given:
# https://prnt.sc/b8M8-S7ZMp_0


# test cases:
# https://prnt.sc/QK6cuxO7iZTX

"""
10
31.3 A
28.4 B
26.1 C
24.2 D
21.8 E
20.3 F
15.5 G
14.1 H
12.5 I
11.5 J
5
32.2 K
27.4 L
24.6 M
14.9 N
13.2 O
"""

# https://prnt.sc/NBT5F-YUrPUA

maxSum = 0.0
problem = Problem()



if __name__ == '__main__':

    clenovi_variables = []
    clenovi_tezhina = []

    lideri_variables = []
    lideri_tezhina = []
    variables_all = []

    broj_clenovi = int(input())

    for i in range(broj_clenovi):
        par = str(input()).split(" ")
        tezhina = float(par[0])
        clenovi_tezhina.append(tezhina)
        clenovi_variables.append(par[1])

    broj_lideri = int(input())

    for i in range(broj_lideri):
        par = input().split(" ")
        tezhina = float(par[0])
        lideri_tezhina.append(tezhina)
        lideri_variables.append(par[1])

    problem.addVariable(1,Domain(lideri_tezhina))
    problem.addVariable(range(2,7), Domain(clenovi_tezhina))

    problem.addConstraint(AllDifferentConstraint(), [1,2,3,4,5,6])
    problem.addConstraint(MaxSumConstraint(100), [1,2,3,4,5,6])

    print(problem.getSolution())