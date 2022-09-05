
"""
Да се дефинира класа за Агент кој ја чува својата позиција
(координати x и y) во некој простор.

Да се дефинира метод кој го означува движењето на агентот во просторот.

Потоа да се дефинираат агенти кои имплементираат специфично
движење (лево, десно, горе, долу).
Извршете 5 движења за секој од агентите и испечатете ја позицијата на агентот во секој чекор.


"""

class Agent:
    def __init__(self,x = 0, y = 0):
        self.x = x
        self.y = y

    def move(self):
        pass

    def __repr__(self):
        return f'Position: ({self.x}, {self.y})'

class LeftAgent(Agent):
    def __init__(self,x=0,y=0):
        super().__init__(x,y)

    def move(self):
        self.x -= 1

class RightAgent(Agent):
    def __init__(self,x,y):
        super(RightAgent, self).__init__(x,y)
    def move(self):
        self.x += 1

class UpAgent(Agent):
    def __init__(self,x,y):
        super(UpAgent, self).__init__(x,y)

    def move(self):
        self.y += 1

class DownAgent(Agent):
    def __init__(self,x,y):
        super(DownAgent, self).__init__(x,y)

    def move(self):
        self.y -= 1



if __name__ == "__main__":
    print()

    la = LeftAgent(3,4)

    for i in range(5):
        la.move()
        print(la)

    ra = RightAgent(5,0)
    for i in range(5):
        ra.move()
        print(ra)