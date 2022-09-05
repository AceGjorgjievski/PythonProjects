"""
This is denotation for the function bellow:

:param pacman: (x,y) -> position of the pacman
:param ghost: (x,y) -> position of the ghost
:param obstacles: ((x0,y0),(x1, y1), (x2, y2), ....) -> tuple od tuples denoting the position of every obstacle
:param m: -> width of the maze
:param n: -> height of the maze
:return: x - > if the agent is moving left or right
:return: y -> if the agent is moving up or down

** after this, in the successors function will be checked if
the old position is not equal with the current new position, then
replace in the successors' dictionary with the current
move ["right,left,up or down"] = (px or px_new, py or py_new, ghost_x, ghost_y,
                                    tuple([f for t in treasure if [px or px_new, py or py_new] != [t[0],t[1]]]))
//the tuple for the treasure will be updated if the position is different with one of the pacman agents, and
checking after if the length of the tuple is 0, and if it is, then it is end.

**Note: in line 14 it depends on what move will be executed, that's why it is concatenated with the 'or' word;
same meaning for the line 13 [right,left,up or down] and for px and py / px_new or py_new

"""
def move_right(pacman, ghost, obstacles, m, n):
    # right
    px, py = pacman
    gx, gy = ghost
    if px + 1 != gx and py != gy and (px + 1, py) not in obstacles and 0 < (px + 1) < n:
        px += 1
    return px

def move_left(pacman, ghost, obstacles, m, n):
    # right
    px, py = pacman
    gx, gy = ghost
    if px - 1 != gx and py != gy and (px - 1, py) not in obstacles and 0 < px < n:
        px -= 1
    return px

def move_up(pacman, ghost, obstacles, m, n):
    # right
    px, py = pacman
    gx, gy = ghost
    if px != gx and py + 1 != gy and (px, py + 1) not in obstacles and 0 < (py + 1) < m:
        py += 1
    return py

def move_down(pacman, ghost, obstacles, m, n):
    # right
    px, py = pacman
    gx, gy = ghost
    if px != gx and py - 1 != gy and (px, py - 1) not in obstacles and 0 < py < m:
        py -= 1
    return py



if __name__ == '__main__':
    pass
