import unittest
from Board.board import Board
from SnakesAndLadders.snakesandladders import SnakeAndLadder
from Player.player import Player
from Utility.utility import Utility
from Game.game import Game

class TestUtility(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Called once before any tests in this class are executed."""
        print("\nSetting up the test class for Utility tests...")

    @classmethod
    def tearDownClass(cls):
        """Called once after all tests in this class have been executed."""
        print("\nTearing down the test class for Utility tests...")

    def setUp(self):
        """Called before every individual test."""
        print("\nSetting up for a test in the Utility test class...")

    def tearDown(self):
        """Called after each individual test."""
        print("\nTearing down after a test in the Utility test class...")

    def test_roll_dice(self):
        """Test the dice roll function."""
        for _ in range(100):  # Test dice roll multiple times
            roll = Utility.roll_dice()
            self.assertIn(roll, range(1, 7), f"Dice roll {roll} is out of range, should be between 1 and 6")

    def test_ascii(self):
        """Test the ASCII art display functionality."""
        # Display ASCII Art at the start of the game
        Utility.display_ascii_art("WELCOME TO SNAKES AND LADDERS")  # Call the function from the utilities module to display ASCII

        # Display ASCII Art at the end of the game
        Utility.display_ascii_art("YOU WIN")  # Call the function from the utilities module to display ASCII art

