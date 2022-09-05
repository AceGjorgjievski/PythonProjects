

"""

Користејќи list comprehension дадена матрица составена од
броеви да се промени секој елемент така што ќе се помножи со 2.

Секој елемент на матрицата се чита од тастатура така што прво се
читаат N и M (број на редици и колони) а потоа во секој ред се
читаат елементите одделени со празно место

4
4
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4

Пример влез: 4 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4

Излез: [[2, 4, 6, 8], [2, 4, 6, 8], [2, 4, 6, 8], [2, 4, 6, 8]]

"""



if __name__ == "__main__":
    n = int(input())
    m = int(input())

    matrix = []
    #
    #
    # for i in range(n):
    #     local = []
    #     for j in range(m):
    #         num = int(input())
    #         local.append(num)
    #     matrix.append(local)
    #
    # print([for x in])

    for i in range(n):
        row = [int(i) for i in input().split(" ")]
        matrix.append(row)

    print(matrix)

    def fun(elem):
        return elem*2

    rez = [[elem*2 for elem in row] for row in matrix] # cela nova matrica
    rez2 = [i*2 for i in matrix for i in row] # cela nova lista
    rez3 = [[fun(matrix[i][j]) for j in range(m)] for i in range(n)] # cela nova matrica 2or nachin
    print(rez)
    print(rez2)
    print(rez3)



