class FibNum:
    def __init__(self):
        self.fn2 = 1
        self.fn1 = 1
    def __next__(self):
        (self.fn1, self.fn2, old_fn2) = (self.fn1 + self.fn2, self.fn1, self.fn2)
        if old_fn2 > 100:
            raise StopIteration
        return old_fn2

    def __iter__(self):
        return self