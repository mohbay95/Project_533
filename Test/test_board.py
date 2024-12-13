import unittest
from Board.board import Board
from Board.board import InvalidPositionError
from SnakesAndLadders.snakesandladders import SnakeAndLadder
from Player.player import Player
from Utility.utility import Utility
from Game.game import Game


class TestBoard(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Called once before any tests in this class are executed."""
        print("\nSetting up the test class for Board tests...")

    @classmethod
    def tearDownClass(cls):
        """Called once after all tests in this class have been executed."""
        print("\nTearing down the test class for Board tests...")

    def setUp(self):
        """Called before every individual test."""
        print("\nSetting up for a test in the Board test class...")
        self.board = Board()  # Initialize a new Board object before each test
        # Initialize player positions, snakes, and ladders
        self.player_positions = [1, 1]  # Player 1 at position 1, Player 2 at position 3
        self.snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
        self.ladders = {4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

    def tearDown(self):
        """Called after each individual test."""
        print("\nTearing down after a test in the Board test class...")
        self.board = None  # Cleanup the board after each test

    def test_initial_board_size(self):
        """Test the initial size of the board."""
        self.assertEqual(self.board.get_size(), 100, "Board size should be 100 by default")

    def test_both_players_same_position(self):
        """Test if both players are displayed correctly at the same position."""
        self.player_positions = [1, 1]  # Both players at position 1
        self.board.print_board_with_emojis(self.player_positions, self.snakes, self.ladders)
        display_board = self.board.get_display_board()
        self.assertEqual(display_board[0], '🔴')  # Both players at position 1


    def test_player_move_valid(self):
       """Test if a player moves to the correct position after rolling the dice."""
       self.player_positions = [1, 1]  # Both players at position 1
       roll = 4  # Simulate a dice roll of 4
       new_position = self.player_positions[0] + roll
       self.player_positions[0] = new_position  # Update player 1's position

       self.board.print_board_with_emojis(self.player_positions, self.snakes, self.ladders)
       display_board = self.board.get_display_board()
       self.assertEqual(display_board[roll], '🔵')  # Player 1 should be at position 5 after rolling 4


    







