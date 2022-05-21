from abc import ABC


class Module(ABC):
    type = -1


class Resolve(Module):

    def __init__(self,adjacent_mines):
        self.adjacent_mines = adjacent_mines
        self.remaining = adjacent_mines

    def update(self):
        self.remaining -= 1


class Mine(Module):

    def __init__(self):
        self.type = 1

    def update(self):
        pass

class Blanc(Module):

    def __init__(self):
        self.type = 0

    def update(self):
        pass

