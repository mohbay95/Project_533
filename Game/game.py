from Board.board import Board
from SnakesAndLadders.snakesandladders import SnakeAndLadder
from Player.player import Player
from Player.player import AdvancedPlayer
from Utility.utility import Utility

class Game:
    def __init__(self):
        self.board = Board()
        self.snake_and_ladder = SnakeAndLadder()
        self.players = Player()
        self.current_player = 0  # 0 for Player 1, 1 for Player 2

    def play_turn(self):
        print(f"Player {self.current_player + 1}'s turn (Position: {self.players.get_position(self.current_player)})")
        input("Press Enter to roll the dice... ")
        roll = Utility.roll_dice()  # Use the Utility module for dice rolls
        print(f"Player {self.current_player + 1} rolled a {roll}")

        new_position = self.players.get_position(self.current_player) + roll
        if new_position > self.board.size:
            new_position = self.players.get_position(self.current_player)

        print(f"Player {self.current_player + 1} moves to {new_position}")
        self.players.set_position(self.current_player, new_position)

        if new_position in self.snake_and_ladder.get_snakes():
            print(f"Oh no! Player {self.current_player + 1} landed on a snake at {new_position}, sliding to {self.snake_and_ladder.get_snakes()[new_position]}")
            self.players.set_position(self.current_player, self.snake_and_ladder.get_snakes()[new_position])
        elif new_position in self.snake_and_ladder.get_ladders():
            print(f"Yay! Player {self.current_player + 1} climbed a ladder at {new_position}, climbing to {self.snake_and_ladder.get_ladders()[new_position]}")
            self.players.set_position(self.current_player, self.snake_and_ladder.get_ladders()[new_position])

        self.board.print_board_with_emojis(self.players.get_positions(), self.snake_and_ladder.get_snakes(), self.snake_and_ladder.get_ladders())

        if self.players.get_position(self.current_player) == self.board.size:
            # Display ASCII Art at the end of the game
            Utility.display_ascii_art("YOU WIN")  # Call the function from the utilities module to display ASCII art
            print(f"Player {self.current_player + 1} wins!")
            return True

        self.current_player = 1 - self.current_player
        return False

    def start_game(self):
        # Display ASCII Art at the start of the game
        Utility.display_ascii_art("WELCOME TO SNAKES AND LADDERS")  # Call the function from the utilities module to display ASCII art
        #print("Welcome to Snakes and Ladders!")
        self.board.print_board_with_emojis(self.players.get_positions(), self.snake_and_ladder.get_snakes(), self.snake_and_ladder.get_ladders())
        while True:
            if self.play_turn():
                break





