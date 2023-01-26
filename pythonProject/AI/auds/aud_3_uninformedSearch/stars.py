from pythonProject.AI.searching_framework.utils import Problem
from pythonProject.AI.searching_framework.uninformed_search import *


def k1_gore_levo(kx,ky, bx, by):
    if (kx-1,ky+2) != (bx,by) and 0<kx-1<8 and 0<ky+2<8:
        kx-=1
        ky+=2
    return kx,ky

def k2_gore_desno(kx,ky, bx, by):
    if (kx+1, ky+2) != (bx,by) and 0<kx+1<8 and 0<ky+2<8:
        kx+=1
        ky+=2
    return kx,ky

def k3_desno_gore(kx,ky, bx, by):
    if (kx+2,ky+1) != (bx, by) and 0<kx+2<8 and 0<ky+1<8:
        kx+=2
        ky+=1
    return kx, ky

def k4_desno_dolu(kx,ky, bx, by):
    if (kx+2, ky-1) != (bx,by) and 0<kx+2<8 and 0<ky-1<8:
        kx+=2
        ky-=1
    return kx, ky

def k5_dolu_desno(kx,ky, bx, by):
    if (kx + 1, ky - 2) != (bx, by) and 0<kx+1<8 and 0<ky-2<8:
        kx+=1
        ky-=2
    return kx,ky

def k6_dolu_levo(kx,ky, bx, by):
    if(kx - 1, ky - 2) != (bx, by) and 0<kx-1<8 and 0<ky-2<8:
        kx -= 1
        ky -= 2
    return kx, ky

def k7_levo_gore(kx,ky, bx, by):
    if (kx - 2, ky +1) != (bx, by) and 0<kx-2<8 and 0<ky+1<8:
        kx -=2
        ky +=1
    return kx, ky

def k8_levo_dolu(kx,ky, bx, by):
    if (kx - 2, ky - 1) != (bx, by) and 0<kx-2<8 and 0<ky-1<8:
        kx -=2
        ky -= 1
    return kx, ky



def b1_gore_levo(bx,by,kx,ky):
    if (bx-1,by+1) != (kx,ky) and 0<bx-1<8 and 0<by+1<8:
        bx-=1
        by+=1
    return bx,by

def b2_gore_desno(bx,by,kx,ky):
    if (bx+1,by+1) != (kx,ky) and 0<bx+1<8 and 0<by+1<8:
        bx+=1
        by+=1
    return bx,by

def b3_dolu_levo(bx,by,kx,ky):
    if (bx-1,by-1) != (kx,ky) and 0<bx-1<8 and 0<by-1<8:
        bx-=1
        by-=1
    return bx,by

def b4_dolu_desno(bx,by,kx,ky):
    if (bx+1,by-1) != (kx,ky) and 0<bx+1<8 and 0<by-1<8:
        bx+=1
        by-=1
    return bx,by



class Stars(Problem):
    def __init__(self,initial, goal=None):
        super(Stars, self).__init__(initial, goal)
        self.grid_size = [8,8]

    def successor(self, state):
        successors = dict()

        knight_x = state[0]
        knight_y = state[1]

        bishop_x = state[2]
        bishop_y = state[3]

        star_positions = state[4]

        kx_new, ky_new = k1_gore_levo(knight_x,knight_y,bishop_x,bishop_y)
        if (kx_new,ky_new) != (knight_x,knight_y):
            successors["K1 - UUL"] = (kx_new,ky_new,bishop_x, bishop_y,
                                      tuple([s for s in star_positions if (kx_new,ky_new) != (s[0],s[1])]))

        kx_new, ky_new = k2_gore_desno(knight_x,knight_y,bishop_x,bishop_y)
        if (kx_new,ky_new) != (knight_x,knight_y):
            successors["K2 - UUR"] = (kx_new,ky_new,bishop_x, bishop_y,
                                      tuple([s for s in star_positions if (kx_new,ky_new) != (s[0],s[1])]))

        kx_new, ky_new = k3_desno_gore(knight_x,knight_y,bishop_x,bishop_y)
        if (kx_new,ky_new) != (knight_x,knight_y):
            successors["K3 - RRU"] = (kx_new,ky_new,bishop_x, bishop_y,
                                      tuple([s for s in star_positions if (kx_new,ky_new) != (s[0],s[1])]))
        kx_new, ky_new = k4_desno_dolu(knight_x,knight_y,bishop_x,bishop_y)
        if (kx_new,ky_new) != (knight_x,knight_y):
            successors["K4 - RRD"] = (kx_new,ky_new,bishop_x, bishop_y,
                                      tuple([s for s in star_positions if (kx_new,ky_new) != (s[0],s[1])]))
        kx_new, ky_new = k5_dolu_desno(knight_x,knight_y,bishop_x,bishop_y)
        if (kx_new,ky_new) != (knight_x,knight_y):
            successors["K5 - DDR"] = (kx_new,ky_new,bishop_x, bishop_y,
                                      tuple([s for s in star_positions if (kx_new,ky_new) != (s[0],s[1])]))
        kx_new, ky_new = k6_dolu_levo(knight_x,knight_y,bishop_x,bishop_y)
        if (kx_new,ky_new) != (knight_x,knight_y):
            successors["K6 - DDL"] = (kx_new,ky_new,bishop_x, bishop_y,
                                      tuple([s for s in star_positions if (kx_new,ky_new) != (s[0],s[1])]))
        kx_new, ky_new = k7_levo_gore(knight_x,knight_y,bishop_x,bishop_y)
        if (kx_new,ky_new) != (knight_x,knight_y):
            successors["K7 - LLU"] = (kx_new,ky_new,bishop_x, bishop_y,
                                      tuple([s for s in star_positions if (kx_new,ky_new) != (s[0],s[1])]))
        kx_new, ky_new = k8_levo_dolu(knight_x,knight_y,bishop_x,bishop_y)
        if (kx_new,ky_new) != (knight_x,knight_y):
            successors["K8 - LLD"] = (kx_new,ky_new,bishop_x, bishop_y,
                                      tuple([s for s in star_positions if (kx_new,ky_new) != (s[0],s[1])]))


        bx_new, by_new = b1_gore_levo(bishop_x,bishop_y,knight_x,knight_y)
        if (bx_new, by_new) != (bishop_x, bishop_y):
            successors["B1 - UL"] = (knight_x,knight_y,bx_new,by_new,
                                     tuple([s for s in star_positions if (bx_new, by_new) != (s[0], s[1])]))

        bx_new, by_new = b2_gore_desno(bishop_x,bishop_y,knight_x,knight_y)
        if (bx_new, by_new) != (bishop_x, bishop_y):
            successors["B2 - UR"] = (knight_x,knight_y,bx_new,by_new,
                                     tuple([s for s in star_positions if (bx_new, by_new) != (s[0], s[1])]))
        bx_new, by_new = b3_dolu_levo(bishop_x,bishop_y,knight_x,knight_y)
        if (bx_new, by_new) != (bishop_x, bishop_y):
            successors["B3 - DL"] = (knight_x,knight_y,bx_new,by_new,
                                     tuple([s for s in star_positions if (bx_new, by_new) != (s[0], s[1])]))
        bx_new, by_new = b4_dolu_desno(bishop_x,bishop_y,knight_x,knight_y)
        if (bx_new, by_new) != (bishop_x, bishop_y):
            successors["B4 - DR"] = (knight_x,knight_y,bx_new,by_new,
                                     tuple([s for s in star_positions if (bx_new, by_new) != (s[0], s[1])]))


        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[4]) == 0

if __name__ == "__main__":
    knight = [2, 5]
    bishop = [5, 1]
    stars_pos = ((1, 1), (4,3), (6, 6))
    # stars_pos = ((3,3))

    stars = Stars((knight[0], knight[1], bishop[0], bishop[1], stars_pos))

    result = breadth_first_graph_search(stars)
    print(result.solution())

    # for i in range(len(stars_pos)):
    #     print(stars_pos.index(stars_pos[i]))



