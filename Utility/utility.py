import random
import art  # Import the art package


class Utility:
    @staticmethod
    def roll_dice():
        try:
            roll = random.randint(1, 6)
            if roll < 1 or roll > 6:
                raise ValueError(f"Dice roll out of range: {roll}. Must be between 1 and 6.")
            return roll
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    @staticmethod
    def display_ascii_art(text=None):
        try:
            if text == "WELCOME TO SNAKES AND LADDERS":
                print(art.text2art("SNAKES AND LADDERS"))
            elif text == "CONGRATULATIONS":
                print(art.text2art("CONGRATULATIONS"))
            else:
                raise ValueError(f"Unknown ASCII art text: {text}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
