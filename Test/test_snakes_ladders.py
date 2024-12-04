import unittest
from Board.board import Board
from SnakesAndLadders.snakesandladders import SnakeAndLadder
from Player.player import Player
from Utility.utility import Utility
from Game.game import Game

class TestSnakeAndLadder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Called once before any tests in this class are executed."""
        print("\nSetting up the test class for Snake and Ladder tests...")

    @classmethod
    def tearDownClass(cls):
        """Called once after all tests in this class have been executed."""
        print("\nTearing down the test class for Snake and Ladder tests...")

    def setUp(self):
        """Called before every individual test."""
        print("\nSetting up for a test in the Snake and Ladder test class...")
        self.snakes_and_ladders = SnakeAndLadder()  # Initialize a new SnakeAndLadder object before each test

    def tearDown(self):
        """Called after each individual test."""
        print("\nTearing down after a test in the Snake and Ladder test class...")
        self.snakes_and_ladders = None  # Cleanup the SnakeAndLadder object after each test

    def test_snakes_positions(self):
        """Test if the snakes are correctly placed on the board."""
        self.assertIn(16, self.snakes_and_ladders.get_snakes(), "Snake at position 16 should exist")
        self.assertEqual(self.snakes_and_ladders.get_snakes()[16], 6, "Snake at position 16 should lead to position 6")

    def test_ladders_positions(self):
        """Test if the ladders are correctly placed on the board."""
        self.assertIn(4, self.snakes_and_ladders.get_ladders(), "Ladder at position 4 should exist")
        self.assertEqual(self.snakes_and_ladders.get_ladders()[4], 14, "Ladder at position 4 should lead to position 14")
