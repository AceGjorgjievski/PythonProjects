if __name__ == "__main__":
    # -----------------------------------------#
    #                   DICTIONARIES          #

    l1 = [1, 2, 3, 4, 5]
    r = {'ime': 'Ace', 'l': l1}
    # print(r)

    # print(r['ime']) # prikaz na na posle V, prevzemeno od K

    r['x'] = 20  # dodavanje na nov par K,V
    # print(r)

    # p = {} #prezen rechnik
    p = dict({1: "A", 2: "B", 3: "C"})
    # print(p)

    # l = list() # prazna lista
    l = list([1, 2, 3])
    # print(l)

    # print(r.keys()) # lista od site keys
    # print(r.values()) # lista od site values
    # print(r.items()) # vrakja lista od torki od soodvetnite vrednosti

    r2 = {1: 'A', 'a': 6, "*": 89}  # razlichen tip na kluchevi, mozhe od bilo koj ne-mutirachki tip


    # print(r2)

    # ------------------------------------------------------#
    #                   FUNCTIONS                          #

    def add(a, b, c):  # vo momentot koga kje se pratat vrednosti
        return a + b
        # za a i b kako argumenti togash se odreduva tipot na primenlivite
        # a koga kje dojde do return, togash se odreduva kakov tip na vrednost
        # vrakja funkcijata


    # mozhe i predefinirana vrednost na argumentite na f-jata
    # add(a,b=4)
    # NO, posle predifinirana vrednost na argumentite
    # mora ponatamu site argumenti da se predifinirani
    # pr. add(a,b,c = 4, d = 8), a ne add(a,b=4,c)
    # print(add(2))
    # print(add(c=3, b=1, a=8)) # promena na redosled na argumentite, pri samiot povik

    # ako nema return vrakja prazna vrednost (None(void,null,nil))
    # None == False

    # * ako promenime vrednost vo ramki na f-jata,
    # togash taa vrednost kje se promeni celosno i za drugite koi
    # shto referenciraat kon nea (pokazhuvaat)

    # print(add(b=3, c=4, a=8))

    # Nema overload na f-ii, mora celosno nova definicija
    # bidejkji nemame kazhano koj e tipot na argumentite i
    # koj e tipot koj shto go vrakja taa f-ja

    # lambda x: x + 3



    def applier(q, x):
        return q(x)

    # lambda - neimenuvana f-ja koja na kraj dava ednostaven rezultat

    print(applier(lambda x: x+3, 7))
