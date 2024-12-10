import unittest
from Board.board import Board
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
        self.snakes = {16: 6}  # Snake at position 16 leading to 6
        self.ladders = {1: 38}  # Ladder at position 1 leading to 38

    def tearDown(self):
        """Called after each individual test."""
        print("\nTearing down after a test in the Board test class...")
        self.board = None  # Cleanup the board after each test

    def test_initial_board_size(self):
        """Test the initial size of the board."""
        self.assertEqual(self.board.get_size(), 100, "Board size should be 100 by default")
        self.assertEqual(len(self.board.display_board), 100, "Board representation must have 100 squares.")
        self.assertTrue(all(cell == '⬜' for cell in self.board.display_board), "Board must be empty at the start.")
        self.assertNotEqual(self.board.size, 50, "Board size should not be 50 by default.")

    def test_both_players_same_position(self):
        """Test if both players are displayed correctly at the same position."""
        self.player_positions = [1, 1]  # Both players at position 1
        self.board.print_board_with_emojis(self.player_positions, self.snakes, self.ladders)
        display_board = self.board.get_display_board()
        self.assertEqual(display_board[0], '🔴', "Both players at position 1")  # Both players at position 1
        self.assertNotEqual(display_board[1], '🔵', "No player should be in position 2.")
        self.assertNotEqual(display_board[0], '🟡', "Position 1 should not be marked only for player 2.")
        self.assertTrue('🔴' in display_board, "The board should show the icon for both players together.")