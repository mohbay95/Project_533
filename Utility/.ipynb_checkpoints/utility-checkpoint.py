import random
import art  # Import the art package


class Utility:
    @staticmethod
    def roll_dice():
        """Simulate a dice roll and return a value between 1 and 6."""
        return random.randint(1, 6)

    @staticmethod
    def display_ascii_art(text=None):
        if text == "WELCOME TO SNAKES AND LADDERS":
                    print(art.text2art("SNAKES AND LADDERS"))
                    
        else:
                    print(art.text2art("CONGRATULATIONS"))  # Default message for unmatched text
