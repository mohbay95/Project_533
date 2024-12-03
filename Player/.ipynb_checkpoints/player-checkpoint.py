class Player:
    def __init__(self, num_players=2):
        self.positions = [1] * num_players

    def set_position(self, player_index, position):
        self.positions[player_index] = position

    def get_position(self, player_index):
        return self.positions[player_index]

    def get_positions(self):
        return self.positions


class AdvancedPlayer(Player):
    def __init__(self, num_players=2):
        super().__init__(num_players)
        self.dice_rolls = [0] * num_players  # Track the number of rolls for each player
        self.turns_played = [0] * num_players  # Track the number of turns played by each player

    def increment_rolls(self, player_index):
        self.dice_rolls[player_index] += 1

    def increment_turns(self, player_index):
        self.turns_played[player_index] += 1

    def get_rolls(self, player_index):
        return self.dice_rolls[player_index]

    def get_turns(self, player_index):
        return self.turns_played[player_index]