




if __name__ == "__main__":

    # f = open("primer.txt")
    # for i in f: # se zima 1ta linija, pa se printa, pa 2ta, pa se printa itn. (se chitaat edna po edna)
    #   print(len(i))

    # #dolzhina na sekoja linija od dadotekata
    # for i in f.readlines(): # se vrakjaat site linii odednash kako lista i potoa gi pechatime site linii
    #     print(len(i))
    #
    # f.close()

    with open("primer.txt") as f:
        string = f.read()
        for i in string:
            print(i, end="")


    string = "hi.hi.hi"
    rez = string.split('.')
    print(' '.join(rez))








    # words = " h hh h h h"
    #
    # for l in words:
    #     for word in l.split():
    #         print(word)




