
#import math
# from math import *





def mult(num):
    return num*2
def even(num):
    return num%2==0

def exe(j):
    if j > 2:
        return j*3
    return j+0

def filter(j):
    return j%2 == 0

if __name__ == "__main__":

    l = [1,2,3,4,5]
    # print([mult(l[i]) for i in range(len(l))])
    # print([mult(i) for i in l if even(i)])



    # t = ([1,2],[3,4],[5,6])
    # rez = [mult(i) for (i,j) in t]
    # for i in rez:
    #     print(i)

    t = (1,2,3,4,5,6,7,8)
    #5,7,9,11
    #10,14,18,22

    rez = [mult(i) for i in
           [j+2 for j in t if filter(j)]]

    # za if else treba napred da stoi pr. [j+1 if j%2==0 else j+2 for j in t]

    # rez2 = [j+1 if j%2 == 0 else j+2 for j in t]
    # print(rez2)
    # print(rez)

    # money = 2000
    # def add():
    #     #global money;
    #     money = 1 + 2
    #     print(money)
    # print(money)
    # add()

    # l1 = ["aa","bb","cc"]
    #
    # for i in l1:
    #     print(len(i))






