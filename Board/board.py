class Board:
    def __init__(self, size=100):
        self.size = size
        self.display_board = ['⬜' for _ in range(size)]

    def set_display_board(self, new_board):
        self.display_board = new_board

    def get_display_board(self):
        return self.display_board

    def print_board_with_emojis(self, player_positions, snakes, ladders):
        # Reset the board
        self.display_board = ['⬜' for _ in range(self.size)]

        # Mark snakes and ladders
        for snake_start in snakes:
            self.display_board[snake_start - 1] = '🐍'
        for ladder_start in ladders:
            self.display_board[ladder_start - 1] = '🪜'

        # Mark players
        for i, pos in enumerate(player_positions):
            if player_positions[0] == player_positions[1]:
                self.display_board[player_positions[0] - 1] = '🔴'  # Both players
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
