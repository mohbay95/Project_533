class SnakeAndLadder:
    def __init__(self, snakes=None, ladders=None):
        self.snakes = snakes or {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
        self.ladders = ladders or {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

    def set_snakes(self, snakes):
        self.snakes = snakes

    def get_snakes(self):
        return self.snakes

    def set_ladders(self, ladders):
        self.ladders = ladders

    def get_ladders(self):
        return self.ladders
