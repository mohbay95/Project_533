class InvalidPositionError(Exception):
    """Custom exception for invalid player positions."""
    pass

class Player:
    def __init__(self, num_players=2):
        self.positions = [1] * num_players

    def set_position(self, player_index, position):
        try:
            if position < 1 or position > 100:
                raise InvalidPositionError(f"Invalid position: {position}. Position must be between 1 and 100.")
            self.positions[player_index] = position
        except InvalidPositionError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_position(self, player_index):
        try:
            if player_index < 0 or player_index >= len(self.positions):
                raise IndexError("Player index out of range.")
            return self.positions[player_index]
        except IndexError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

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

