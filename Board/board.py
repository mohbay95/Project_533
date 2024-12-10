class InvalidPositionError(Exception):
    """Custom exception for invalid board positions."""
    def __init__(self, message="Position is outside the valid board range"):
        self.message = message
        super().__init__(self.message)

class Board:
    def __init__(self, size=100):
        if not isinstance(size, int) or size <= 0:
            raise ValueError("Board size must be a positive integer.")
        self.size = size
        self.display_board = ['⬜' for _ in range(size)]

    def get_size(self):
        """Returns the size of the board."""
        return self.size

    def set_display_board(self, new_board):
        if not isinstance(new_board, list):
            raise TypeError("Display board must be a list.")
        if len(new_board) != self.size:
            raise ValueError(f"Board size mismatch. Expected size: {self.size}, got: {len(new_board)}.")
        self.display_board = new_board

    def get_display_board(self):
        return self.display_board

    def print_board_with_emojis(self, player_positions, snakes, ladders):
        # Error handling for player positions, snakes, and ladders
        if not isinstance(player_positions, list) or not all(isinstance(pos, int) for pos in player_positions):
            raise TypeError("Player positions must be a list of integers.")
        if not isinstance(snakes, dict) or not isinstance(ladders, dict):
            raise TypeError("Snakes and ladders must be dictionaries.")
        
        # Reset the board
        self.display_board = ['⬜' for _ in range(self.size)]

        # Mark snakes and ladders
        for snake_start in snakes:
            if not (1 <= snake_start <= self.size):
                raise InvalidPositionError(f"Snake starting position {snake_start} is outside the board.")
            self.display_board[snake_start - 1] = '🐍'
        for ladder_start in ladders:
            if not (1 <= ladder_start <= self.size):
                raise InvalidPositionError(f"Ladder starting position {ladder_start} is outside the board.")
            self.display_board[ladder_start - 1] = '🪜'

        # Mark players
        for i, pos in enumerate(player_positions):
            if not (1 <= pos <= self.size):
                raise InvalidPositionError(f"Player position {pos} is outside the board.")
            if player_positions[0] == player_positions[1]:
                self.display_board[pos - 1] = '🔴'  # Both players at same position
                break
            elif pos <= self.size:
                self.display_board[pos - 1] = '🔵' if i == 0 else '🟡'

        print("-" * 85)  # Print horizontal line between rows

        # Print the board row by row
        for i in range(9, -1, -1):  # From bottom to top
            start = i * 10
            end = start + 10
            row = self.display_board[start:end]
            
            if i % 2 == 1:  # Reverse for zigzag
                row = row[::-1]
            formatted_row = ["{:^4}".format(x) for x in row]
            
            print("| " + " | ".join(formatted_row)+ "|")
            
            # Print a horizontal line after each row except the last one
            if i >= 0:
               print("-" * 85)
            
        print("\n")
