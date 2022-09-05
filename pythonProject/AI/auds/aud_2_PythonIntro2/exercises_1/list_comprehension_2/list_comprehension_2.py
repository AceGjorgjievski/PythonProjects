

"""
https://github.com/fcse-is/ai/tree/master/av2


Користејќи list comprehension дадена матрица составена од
броеви да се промени секој елемент така што ако припаѓа во
горната половина(индексот на редицата е помеѓу 0 и n/2)
треба да се помножи со 2 а ако припаѓа на долната половина
треба да се помножи со 3. Секој елемент на матрицата се чита
од тастатура така што прво се читаат N и M (број на редици и колони)
а потоа во секој ред се читаат елементите одделени со празно место.


4
4
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4

Пример влез: 4 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4

Излез: [[2, 4, 6, 8], [2, 4, 6, 8], [3, 6, 9, 12], [3, 6, 9, 12]]

"""

def mult(elem,ind,n):
    if ind < n/2:
        return elem*2
    return elem*3



if __name__ == "__main__":
    n = int(input())
    m = int(input())

    matrix = []
    for i in range(n):
        row = [int(i) for i in input().split(" ")]
        matrix.append(row)
    # print(matrix)

    rez = [[mult(matrix[i][j],i,n) for j in range(m)] for i in range(n)]
    print(rez)



