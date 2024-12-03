# main.py

from Board.board import Board
from SnakesAndLadders.snakesandladders import SnakeAndLadder
from Player.player import Player
from Utility.utility import Utility
from Game.game import Game


import unittest

# Import the test classes
from Test.test_game import TestGame
from Test.test_player import TestPlayer
from Test.test_snakes_ladders import TestSnakeAndLadder
from Test.test_util import TestUtility
from Test.test_board import TestBoard

# Create a test suite
def suite():
    suite = unittest.TestSuite()

    # Add individual test cases (classes) to the suite
    suite.addTest(unittest.makeSuite(TestGame))
    suite.addTest(unittest.makeSuite(TestPlayer))
    suite.addTest(unittest.makeSuite(TestSnakeAndLadder))
    suite.addTest(unittest.makeSuite(TestUtility))
    suite.addTest(unittest.makeSuite(TestBoard))

    return suite

# Run the test suite
runner = unittest.TextTestRunner()
runner.run(suite())
# from game import Game

 if __name__ == "__main__":
      game = Game()
      game.play_game()


