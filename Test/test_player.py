import unittest
from Board.board import Board
from SnakesAndLadders.snakesandladders import SnakeAndLadder
from Player.player import Player
from Utility.utility import Utility
from Game.game import Game

class TestPlayer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Called once before any tests in this class are executed."""
        print("\nSetting up the test class for Player tests...")

    @classmethod
    def tearDownClass(cls):
        """Called once after all tests in this class have been executed."""
        print("\nTearing down the test class for Player tests...")

    def setUp(self):
        """Called before every individual test."""
        print("\nSetting up for a test in the Player test class...")
        self.players = Player()  # Initialize a new Player object before each test

    def tearDown(self):
        """Called after each individual test."""
        print("\nTearing down after a test in the Player test class...")
        self.players = None  # Cleanup the Player object after each test

    def test_initial_positions(self):
        """Test the initial positions of the players."""
        self.assertEqual(self.players.get_positions(), [1, 1], "Both players should start at position 1")

    def test_update_position(self):
        """Test if the position update works correctly."""
        self.players.set_position(0, 20)
        self.assertEqual(self.players.get_position(0), 20, "Player 1 should move to position 20")
        self.players.set_position(1, 35)
        self.assertEqual(self.players.get_position(1), 35, "Player 2 should move to position 35")


