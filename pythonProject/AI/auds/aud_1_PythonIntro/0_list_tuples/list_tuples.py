if __name__ == "__main__":
    a = [1, 2, 3, 'abc', (10, 20)]
    # print(a)

    b = ('x', 'y', 10.5, [1, 2, 3])
    # print(b)

    c = 'abc'
    # print(c)

    # print(a[-1])
    # print(a[1:-1])

    # print(a[2:])

    d = a[:]  # kopija na torka ili lista
    # print(d)

    # print((10, 20) in a) # dali se naogja elementot vo listata
    # print(100 not in a) # dali elementot ne se naogja vo listata

    # print(a[3][0]) #1ot karakter od 'abc'

    # print("hello" + " " + "world")

    # -------------------------------------------------------------------------------#
    #                            LIST AND TUPLES                                     #
    list1 = [1, 2, 3, 4]
    list2 = [5, 6, 7, 8]
    list3 = list1 + list2  # concat
    # print(list3)

    # print(list1 * 3) # 1,2,3,4,1,2,3,4,1,2,3,4 (3 pati (1,2,3,4))

    # b[0] = 5 # ne mozhe da se promeni torka, unmutable
    # print(list1)

    l1 = [1, 2, 3]
    t1 = (5, 2, 3)

    # l1[1] = 4 # mozhe da se promeni lista bidejkji mutable se
    # print(l1) # 1 4 3

    # kako da se promeni element vo torka
    lt1 = list(t1)  # e da se pretvori torkata vo lista
    lt1[2] = 1  # da se smeni elementot vo listata
    t1 = tuple(lt1)  # i povtorno da se vrati nazad vo torka
    # print(t1)

    l1.append(4)  # element se dodava na kraj od listata
    # print(l1)
    l1.insert(0, 7)  # na 0ta pozicija dodai element 7
    # print(l1)

    l1.append([8, 8, 8])  # se dodavaat elementite kako edna lista
    print(l1)

    l1.extend([9, 9, 9])  # se dodavaat elementite posebno kako so append no ovojpat
    # print(l1) # kolku sakame kako celina, mozheshe i so l1 + [9,9,9]

    # append i extend mozhe da se zbunime

    l1.append(3)
    # print(l1)
    # print(l1.count(3)) # kolku pati se pojavuva elementot '3' vo listata
    # print(l1.index(3)) # go pechati indexot na prvoto pojavuvanje na elementot '3'

    l1.remove(3)  # go brishe 1to pojavuvanje na elementot '3'
    # print(l1)

    l1.reverse()  # go menuva redosledot na elementite
    # print(l1)

    l2 = [5, 2, "abc", 7, 1]  # ne mozhe sort od razlichni tipovi na promenlivi
    # print(l2)
    # l2.sort() # sort error
    # print(l2)

    # print(str(5))  # cast od eden vo dr tip: drug format na cast: str(), int(), float()
    # 5.0

    # ---------------------------------------------------------#
