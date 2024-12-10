class SnakeAndLadder:
    def __init__(self, snakes=None, ladders=None):
        self.snakes = snakes or {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
        self.ladders = ladders or {4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

    def set_snakes(self, snakes):
        try:
            if not isinstance(snakes, dict):
                raise TypeError("Snakes must be a dictionary.")
            for start, end in snakes.items():
                if start <= end:
                    raise ValueError(f"Invalid snake: Head should be at a higher position than tail (Start: {start}, End: {end})")
            self.snakes = snakes
        except (TypeError, ValueError) as e:
            print(f"Error setting snakes: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def set_ladders(self, ladders):
        try:
            if not isinstance(ladders, dict):
                raise TypeError("Ladders must be a dictionary.")
            for start, end in ladders.items():
                if start >= end:
                    raise ValueError(f"Invalid ladder: Bottom should be at a lower position than top (Start: {start}, End: {end})")
            self.ladders = ladders
        except (TypeError, ValueError) as e:
            print(f"Error setting ladders: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_snakes(self):
        return self.snakes

    def get_ladders(self):
        return self.ladders
