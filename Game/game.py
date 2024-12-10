from Board.board import Board
from SnakesAndLadders.snakesandladders import SnakeAndLadder
from Player.player import Player
#from Player.player import AdvancedPlayer
from Utility.utility import Utility


# class Game:
#     def __init__(self):
#         self.board = Board()
#         self.snake_and_ladder = SnakeAndLadder()
#         self.players = Player()
#         self.current_player = 0

#     def play_turn(self):
#         try:
#             print(f"Player {self.current_player + 1}'s turn (Position: {self.players.get_position(self.current_player)})")
#             input("Press Enter to roll the dice... ")
#             roll = Utility.roll_dice()  # Simulating a dice roll
#             if roll < 1 or roll > 6:
#                 raise ValueError(f"Invalid dice roll: {roll}. Must be between 1 and 6.")
#             print(f"Player {self.current_player + 1} rolled a {roll}")
            
#             new_position = self.players.get_position(self.current_player) + roll
#             if new_position > self.board.size:
#                 new_position = self.players.get_position(self.current_player)

#             print(f"Player {self.current_player + 1} moves to {new_position}")
#             self.players.set_position(self.current_player, new_position)
            

#             # Handle snakes and ladders
#             if new_position in self.snake_and_ladder.get_snakes():
#                  print(f"Oh no! Player {self.current_player + 1} landed on a snake at {new_position}, sliding to {self.snake_and_ladder.get_snakes()[new_position]}")
#                  self.players.set_position(self.current_player, self.snake_and_ladder.get_snakes()[new_position])

                
#             elif new_position in self.snake_and_ladder.get_ladders():
#                  print(f"Yay! Player {self.current_player + 1} climbed a ladder at {new_position}, climbing to {self.snake_and_ladder.get_ladders()[new_position]}")
#                  self.players.set_position(self.current_player, self.snake_and_ladder.get_ladders()[new_position])

                
#             self.board.print_board_with_emojis(self.players.get_positions(), self.snake_and_ladder.get_snakes(), self.snake_and_ladder.get_ladders())
            
#             if self.players.get_position(self.current_player) == self.board.size:
#                  Utility.display_ascii_art("CONGRATULATIONS")  # Call the function from the utilities module to display ASCII art
#                  print(f"Player {self.current_player + 1} wins!")
#                  return True

           
#             self.current_player = 1 - self.current_player
#             return False

#         except ValueError as e:
#             print(f"Error: {e}")
#         except Exception as e:
#             print(f"Unexpected error: {e}")

#     def start_game(self):
#         try:
#             print("Starting the game...")
#             # Display ASCII Art at the start of the game
#             Utility.display_ascii_art("WELCOME TO SNAKES AND LADDERS")  # Call the function from the utilities module to display ASCII art
#             print("Welcome to Snakes and Ladders!")
#             self.board.print_board_with_emojis(self.players.get_positions(), self.snake_and_ladder.get_snakes(), self.snake_and_ladder.get_ladders())

#             while True:
#                 if self.play_turn():
#                     break
#         except Exception as e:
#             print(f"Unexpected error in game loop: {e}")






class Game:
    def __init__(self):
        self.board = Board()
        self.snake_and_ladder = SnakeAndLadder()
        self.players = Player()
        self.current_player = 0

    def handle_snakes_and_ladders(self, position):
        """
        Handle scenarios where a player lands on a snake or a ladder.
        """
        if position in self.snake_and_ladder.get_snakes():
            new_position = self.snake_and_ladder.get_snakes()[position]
            print(f"Oh no! Player {self.current_player + 1} landed on a snake at {position}, sliding to {new_position}")
            return new_position
        elif position in self.snake_and_ladder.get_ladders():
            new_position = self.snake_and_ladder.get_ladders()[position]
            print(f"Yay! Player {self.current_player + 1} climbed a ladder at {position}, climbing to {new_position}")
            return new_position
        return position

    def check_winning_condition(self):
        """
        Check if the current player has won the game.
        """
        if self.players.get_position(self.current_player) == self.board.size:
            Utility.display_ascii_art("CONGRATULATIONS")
            print(f"Player {self.current_player + 1} wins!")
            return True
        return False

    def play_turn(self):
        try:
            print(f"Player {self.current_player + 1}'s turn (Position: {self.players.get_position(self.current_player)})")
            input("Press Enter to roll the dice... ")
            roll = Utility.roll_dice()  # Simulating a dice roll
            if roll < 1 or roll > 6:
                raise ValueError(f"Invalid dice roll: {roll}. Must be between 1 and 6.")
            print(f"Player {self.current_player + 1} rolled a {roll}")
            
            new_position = self.players.get_position(self.current_player) + roll
            if new_position > self.board.size:
                new_position = self.players.get_position(self.current_player)

            print(f"Player {self.current_player + 1} moves to {new_position}")
            new_position = self.handle_snakes_and_ladders(new_position)  # Check for snakes and ladders
            self.players.set_position(self.current_player, new_position)

            self.board.print_board_with_emojis(self.players.get_positions(), self.snake_and_ladder.get_snakes(), self.snake_and_ladder.get_ladders())
            
            if self.check_winning_condition():  # Check if the player has won
                return True

            self.current_player = 1 - self.current_player
            return False

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


    def start_game(self):
        try:
            print("Starting the game...")
            # Display ASCII Art at the start of the game
            Utility.display_ascii_art("WELCOME TO SNAKES AND LADDERS")  # Call the function from the utilities module to display ASCII art
            print("Welcome to Snakes and Ladders!")
            self.board.print_board_with_emojis(self.players.get_positions(), self.snake_and_ladder.get_snakes(), self.snake_and_ladder.get_ladders())

            while True:
                if self.play_turn():
                    break
        except Exception as e:
            print(f"Unexpected error in game loop: {e}")

