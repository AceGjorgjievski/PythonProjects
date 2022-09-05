"""
Да се напише функција која за дадена листа од торки
во облик [('a', 1), ('b', 2), ('c', 3)] ќе направи swap
на елементите во торките така што елементот на позиција 0 ќе
биде елемент на позиција 1 и обратно. Да се користи list
comprehension.

Пример влез: [('a', 1), ('b', 2), ('c', 3)]

Пример излез: [(1, 'a'), (2, 'b'), (3, 'c')]
"""


def swap(list):
    rez = []
    for (x, y) in list:
        rez.append((y, x))
    return rez

def sw(list):
    return [(y,x) for (x,y) in list]


if __name__ == "__main__":

    l = [('a', 1), ('b', 2), ('c', 3)]

    # rez = [for i in [swap(x,y) for (x,y) in l]]
    # rez = [sw(l) for (x, y) in l]
    #rez2 = [sw(x,y) for (x, y) in l]
    print(sw(l))  # one way
    #print(swap(l))  # second way
