import bisect

"""
Дефинирање на класа за структурата на проблемот кој ќе го решаваме со пребарување.
Класата Problem е апстрактна класа од која правиме наследување за дефинирање на основните 
карактеристики на секој проблем што сакаме да го решиме
"""


class Problem:
    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal

    def successor(self, state):
        """За дадена состојба, врати речник од парови {акција : состојба}
        достапни од оваа состојба. Ако има многу следбеници, употребете
        итератор кој би ги генерирал следбениците еден по еден, наместо да
        ги генерирате сите одеднаш.
        :param state: дадена состојба
        :return:  речник од парови {акција : состојба} достапни од оваа
                  состојба
        :rtype: dict
        """
        raise NotImplementedError

    def actions(self, state):
        """За дадена состојба state, врати листа од сите акции што може да
        се применат над таа состојба
        :param state: дадена состојба
        :return: листа на акции
        :rtype: list
        """
        raise NotImplementedError

    def result(self, state, action):
        """За дадена состојба state и акција action, врати ја состојбата
        што се добива со примена на акцијата над состојбата
        :param state: дадена состојба
        :param action: дадена акција
        :return: резултантна состојба
        """
        raise NotImplementedError

    def goal_test(self, state):
        """Врати True ако state е целна состојба. Даденава имплементација
        на методот директно ја споредува state со self.goal, како што е
        специфицирана во конструкторот. Имплементирајте го овој метод ако
        проверката со една целна состојба self.goal не е доволна.
        :param state: дадена состојба
        :return: дали дадената состојба е целна состојба
        :rtype: bool
        """
        return state == self.goal

    def path_cost(self, c, state1, action, state2):
        """Врати ја цената на решавачкиот пат кој пристигнува во состојбата
        state2 од состојбата state1 преку акцијата action, претпоставувајќи
        дека цената на патот до состојбата state1 е c. Ако проблемот е таков
        што патот не е важен, оваа функција ќе ја разгледува само состојбата
        state2. Ако патот е важен, ќе ја разгледува цената c и можеби и
        state1 и action. Даденава имплементација му доделува цена 1 на секој
        чекор од патот.
        :param c: цена на патот до состојбата state1
        :param state1: дадена моментална состојба
        :param action: акција која треба да се изврши
        :param state2: состојба во која треба да се стигне
        :return: цена на патот по извршување на акцијата
        :rtype: float
        """
        return c + 1

    def value(self):
        """За проблеми на оптимизација, секоја состојба си има вредност.
        Hill-climbing и сличните алгоритми се обидуваат да ја максимизираат
        оваа вредност.
        :return: вредност на состојба
        :rtype: float
        """
        raise NotImplementedError


"""
Дефинирање на класата за структурата на јазел од пребарување.
Класата Node не се наследува
"""


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Креирај јазол од пребарувачкото дрво, добиен од parent со примена
        на акцијата action
        :param state: моментална состојба (current state)
        :param parent: родителска состојба (parent state)
        :param action: акција (action)
        :param path_cost: цена на патот (path cost)
        """
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0  # search depth
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node %s>" % (self.state,)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        """Излистај ги јазлите достапни во еден чекор од овој јазол.
        :param problem: даден проблем
        :return: листа на достапни јазли во еден чекор
        :rtype: list(Node)
        """

        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        """Дете јазел
        :param problem: даден проблем
        :param action: дадена акција
        :return: достапен јазел според дадената акција
        :rtype: Node
        """
        next_state = problem.result(self.state, action)
        return Node(next_state, self, action,
                    problem.path_cost(self.path_cost, self.state,
                                      action, next_state))

    def solution(self):
        """Врати ја секвенцата од акции за да се стигне од коренот до овој јазол.
        :return: секвенцата од акции
        :rtype: list
        """
        return [node.action for node in self.path()[1:]]

    def solve(self):
        """Врати ја секвенцата од состојби за да се стигне од коренот до овој јазол.
        :return: листа од состојби
        :rtype: list
        """
        return [node.state for node in self.path()[0:]]

    def path(self):
        """Врати ја листата од јазли што го формираат патот од коренот до овој јазол.
        :return: листа од јазли од патот
        :rtype: list(Node)
        """
        x, result = self, []
        while x:
            result.append(x)
            x = x.parent
        result.reverse()
        return result

    """Сакаме редицата од јазли кај breadth_first_search или 
    astar_search да не содржи состојби - дупликати, па јазлите што
    содржат иста состојба ги третираме како исти. [Проблем: ова може
    да не биде пожелно во други ситуации.]"""

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)


"""
Дефинирање на помошни структури за чување на листата на генерирани, но непроверени јазли
"""


class Queue:
    """Queue е апстрактна класа / интерфејс. Постојат 3 типа:
        Stack(): Last In First Out Queue (стек).
        FIFOQueue(): First In First Out Queue (редица).
        PriorityQueue(order, f): Queue во сортиран редослед (подразбирливо,од најмалиот кон
                                 најголемиот јазол).
    """

    def __init__(self):
        raise NotImplementedError

    def append(self, item):
        """Додади го елементот item во редицата
        :param item: даден елемент
        :return: None
        """
        raise NotImplementedError

    def extend(self, items):
        """Додади ги елементите items во редицата
        :param items: дадени елементи
        :return: None
        """
        raise NotImplementedError

    def pop(self):
        """Врати го првиот елемент од редицата
        :return: прв елемент
        """
        raise NotImplementedError

    def __len__(self):
        """Врати го бројот на елементи во редицата
        :return: број на елементи во редицата
        :rtype: int
        """
        raise NotImplementedError

    def __contains__(self, item):
        """Проверка дали редицата го содржи елементот item
        :param item: даден елемент
        :return: дали queue го содржи item
        :rtype: bool
        """
        raise NotImplementedError


class Stack(Queue):
    """Last-In-First-Out Queue."""

    def __init__(self):
        self.data = []

    def append(self, item):
        self.data.append(item)

    def extend(self, items):
        self.data.extend(items)

    def pop(self):
        return self.data.pop()

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data


class FIFOQueue(Queue):
    """First-In-First-Out Queue."""

    def __init__(self):
        self.data = []

    def append(self, item):
        self.data.append(item)

    def extend(self, items):
        self.data.extend(items)

    def pop(self):
        return self.data.pop(0)

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data


class PriorityQueue(Queue):
    """Редица во која прво се враќа минималниот (или максималниот) елемент
    (како што е определено со f и order). Оваа структура се користи кај
    информирано пребарување"""
    """"""

    def __init__(self, order=min, f=lambda x: x):
        """
        :param order: функција за подредување, ако order е min, се враќа елементот
                      со минимална f(x); ако order е max, тогаш се враќа елементот
                      со максимална f(x).
        :param f: функција f(x)
        """
        assert order in [min, max]
        self.data = []
        self.order = order
        self.f = f

    def append(self, item):
        bisect.insort_right(self.data, (self.f(item), item))

    def extend(self, items):
        for item in items:
            bisect.insort_right(self.data, (self.f(item), item))

    def pop(self):
        if self.order == min:
            return self.data.pop(0)[1]
        return self.data.pop()[1]

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return any(item == pair[1] for pair in self.data)

    def __getitem__(self, key):
        for _, item in self.data:
            if item == key:
                return item

    def __delitem__(self, key):
        for i, (value, item) in enumerate(self.data):
            if item == key:
                self.data.pop(i)


import sys

"""
Неинформирано пребарување во рамки на дрво.
Во рамки на дрвото не разрешуваме јамки.
"""


def tree_search(problem, fringe):
    """ Пребарувај низ следбениците на даден проблем за да најдеш цел.
    :param problem: даден проблем
    :type problem: Problem
    :param fringe:  празна редица (queue)
    :type fringe: FIFOQueue or Stack or PriorityQueue
    :return: Node or None
    :rtype: Node
    """
    fringe.append(Node(problem.initial))
    while fringe:
        node = fringe.pop()
        print(node.state)
        if problem.goal_test(node.state):
            return node
        fringe.extend(node.expand(problem))
    return None


def breadth_first_tree_search(problem):
    """Експандирај го прво најплиткиот јазол во пребарувачкото дрво.
    :param problem: даден проблем
    :type problem: Problem
    :return: Node or None
    :rtype: Node
    """
    return tree_search(problem, FIFOQueue())


def depth_first_tree_search(problem):
    """Експандирај го прво најдлабокиот јазол во пребарувачкото дрво.
    :param problem: даден проблем
    :type problem: Problem
    :return: Node or None
    :rtype: Node
    """
    return tree_search(problem, Stack())


"""
Неинформирано пребарување во рамки на граф
Основната разлика е во тоа што овде не дозволуваме јамки, 
т.е. повторување на состојби
"""


def graph_search(problem, fringe):
    """Пребарувај низ следбениците на даден проблем за да најдеш цел.
     Ако до дадена состојба стигнат два пата, употреби го најдобриот пат.
    :param problem: даден проблем
    :type problem: Problem
    :param fringe:  празна редица (queue)
    :type fringe: FIFOQueue or Stack or PriorityQueue
    :return: Node or None
    :rtype: Node
    """
    closed = set()
    fringe.append(Node(problem.initial))
    while fringe:
        node = fringe.pop()
        if problem.goal_test(node.state):
            return node
        if node.state not in closed:
            closed.add(node.state)
            fringe.extend(node.expand(problem))
    return None


def breadth_first_graph_search(problem):
    """Експандирај го прво најплиткиот јазол во пребарувачкиот граф.
    :param problem: даден проблем
    :type problem: Problem
    :return: Node or None
    :rtype: Node
    """
    return graph_search(problem, FIFOQueue())


def depth_first_graph_search(problem):
    """Експандирај го прво најдлабокиот јазол во пребарувачкиот граф.
    :param problem: даден проблем
    :type problem: Problem
    :return: Node or None
    :rtype: Node
    """
    return graph_search(problem, Stack())


def depth_limited_search(problem, limit=50):
    """Експандирај го прво најдлабокиот јазол во пребарувачкиот граф
    со ограничена длабочина.
    :param problem: даден проблем
    :type problem: Problem
    :param limit: лимит за длабочината
    :type limit: int
    :return: Node or None
    :rtype: Node
    """

    def recursive_dls(node, problem, limit):
        """Помошна функција за depth limited"""
        cutoff_occurred = False
        if problem.goal_test(node.state):
            return node
        elif node.depth == limit:
            return 'cutoff'
        else:
            for successor in node.expand(problem):
                result = recursive_dls(successor, problem, limit)
                if result == 'cutoff':
                    cutoff_occurred = True
                elif result is not None:
                    return result
        if cutoff_occurred:
            return 'cutoff'
        return None

    return recursive_dls(Node(problem.initial), problem, limit)


def iterative_deepening_search(problem):
    """Експандирај го прво најдлабокиот јазол во пребарувачкиот граф
    со ограничена длабочина, со итеративно зголемување на длабочината.
    :param problem: даден проблем
    :type problem: Problem
    :return: Node or None
    :rtype: Node
    """
    for depth in range(sys.maxsize):
        result = depth_limited_search(problem, depth)
        if result != 'cutoff':
            return result


def uniform_cost_search(problem):
    """Експандирај го прво јазолот со најниска цена во пребарувачкиот граф.
    :param problem: даден проблем
    :type problem: Problem
    :return: Node or None
    :rtype: Node
    """
    return graph_search(problem, PriorityQueue(min, lambda a: a.path_cost))


def move_right(x, y, obstacles):
    if 0 < x + 1 < 10 and (x + 1, y) not in obstacles:
        x += 1
    return x


def move_left(x, y, obstacles):
    if 0 <= x - 1 < 10 and (x - 1, y) not in obstacles:
        x -= 1
    return x


def move_up(x, y, obstacles):
    if 0 <= y + 1 < 10 and (x, y + 1) not in obstacles:
        y += 1
    return y


def move_down(x, y, obstacles):
    if 0 <= y - 1 < 10 and (x, y - 1) not in obstacles:
        y -= 1
    return y


class Pacman(Problem):
    def __init__(self, initial,obstacles, goal=None):
        super(Pacman, self).__init__(initial, goal)
        self.grid_size = [10, 10]
        self.obstacles = obstacles

    def successor(self, state):
        successor = {}

        px = state[0]
        py = state[1]
        dir = state[2]

        food = state[3]


        if dir == "istok":
            if 0<px+1<self.grid_size[0] and (px+1, py) not in self.obstacles:
                successor["ProdolzhiPravo"] = (px+1, py, "istok",
                                               tuple([f for f in food if [px+1, py] != [f[0], f[1]]]))
            if 0 < px < self.grid_size[0] and (px-1, py) not in self.obstacles:
                successor["ProdolzhiNazad"] = (px-1, py, "zapad",
                                               tuple([f for f in food if [px-1, py] != [f[0], f[1]]]))
            if 0 < py + 1< self.grid_size[1] and (px, py+1) not in self.obstacles:
                successor["SvrtiLevo"] = (px, py+1, "sever",
                                          tuple([f for f in food if [px, py+1] != [f[0], f[1]]]))

            if 0 < py < self.grid_size[1] and (px, py-1) not in self.obstacles:
                successor["SvrtiDesno"] = (px, py-1, "jug",
                                          tuple([f for f in food if [px, py-1] != [f[0], f[1]]]))

        if dir == "zapad":
            if 0<px<self.grid_size[0] and (px-1, py) not in self.obstacles:
                successor["ProdolzhiPravo"] = (px-1, py, "zapad",
                                           tuple([f for f in food if [px-1, py] != [f[0], f[1]]]))

            if 0<px+1<self.grid_size[0] and(px+1, py) not in self.obstacles:
                successor["ProdolzhiNazad"] = (px+1, py, "istok",
                                           tuple([f for f in food if [px+1, py] != [f[0], f[1]]]))

            if 0 < py < self.grid_size[1] and (px, py-1) not in self.obstacles:
                successor["SvrtiLevo"] = (px, py-1, "jug",
                                          tuple([f for f in food if [px, py-1] != [f[0], f[1]]]))

            if 0<py+1<self.grid_size[1] and (px, py+1) not in self.obstacles:
                successor["SvrtiDesno"] = (px, py+1, "sever",
                                          tuple([f for f in food if [px, py+1] != [f[0], f[1]]]))



        if dir == "sever":
            if 0<py+1<self.grid_size[1] and (px, py+1) not in self.obstacles:
                successor["ProdolzhiPravo"] = (px, py+1, "sever",
                                          tuple([f for f in food if [px, py+1] != [f[0], f[1]]]))

            if 0<py<self.grid_size[1] and (px, py-1) not in self.obstacles:
                successor["ProdolzhiNazad"] = (px, py-1, "jug",
                                          tuple([f for f in food if [px, py-1] != [f[0], f[1]]]))

            if 0<px<self.grid_size[0] and (px-1, py) not in self.obstacles:
                successor["SvrtiLevo"] = (px-1, py, "zapad",
                                           tuple([f for f in food if [px-1, py] != [f[0], f[1]]]))

            if 0<px+1<self.grid_size[0] and (px+1, py) not in self.obstacles:
                successor["SvrtiDesno"] = (px+1, py, "istok",
                                           tuple([f for f in food if [px+1, py] != [f[0], f[1]]]))

        if dir == "jug":
            if 0<py<self.grid_size[1] and (px, py-1) not in self.obstacles:
                successor["ProdolzhiPravo"] = (px, py-1, "jug",
                                          tuple([f for f in food if [px, py-1] != [f[0], f[1]]]))

            if 0 <py+1< self.grid_size[1] and (px, py+1) not in self.obstacles:
                successor["ProdolzhiNazad"] = (px, py+1, "sever",
                                          tuple([f for f in food if [px, py+1] != [f[0], f[1]]]))

            if 0<px+1<self.grid_size[0] and (px+1, py) not in self.obstacles:
                successor["SvrtiLevo"] = (px+1, py, "istok",
                                           tuple([f for f in food if [px+1, py] != [f[0], f[1]]]))

            if 0<px<self.grid_size[0] and (px-1, py) not in self.obstacles:
                successor["SvrtiDesno"] = (px-1, py, "zapad",
                                          tuple([f for f in food if [px-1, py] != [f[0], f[1]]]))






        return successor

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[3]) == 0


if __name__ == "__main__":
    px = int(input())
    py = int(input())
    dir = str(input())

    food_num = int(input())
    food_pos = []

    obstacles = ((0, 9), (0, 8), (0, 6),
                 (1, 2), (1, 3), (1, 4), (1, 9),
                 (2, 9),
                 (3, 9), (3, 6),
                 (4, 6), (4, 7), (4, 5), (4, 1),
                 (5, 1), (5, 6),
                 (6, 9), (6, 0), (6, 1), (6, 2),
                 (8, 1), (8, 4), (8, 7), (8, 8),
                 (9, 4), (9, 7), (9, 8))

    for i in range(0, food_num):
        pos = input().split(", ")
        pos_x = int(pos[0].split(",")[0])
        pos_y = int(pos[0].split(",")[1])
        temp = []
        temp.append(pos_x)
        temp.append(pos_y)
        food_pos.append(tuple(temp))

    pacman = Pacman((px, py, dir, tuple(food_pos)), obstacles)

    result = breadth_first_graph_search(pacman)

    print(result.solution())

    # for i in range(len(food_pos)):
    #     print(food_pos[i])
    #
    # print(tuple(food_pos))
