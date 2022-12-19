"""Main module for the seven little words game.

Author: Aidan Chadha
Version: 12/5/2022
"""

from game_info import GameInfo
from game_board import GameBoard
import sys
import os


class SevenLittleWords:
    """Seven little words class."""
    
    if __name__ == "__main__":
        if len(sys.argv) != 2 or len(sys.argv) is None:
            print('Usage: python seven_little_words.py <game_file>')
            sys.exit(1)
        elif not os.path.exists(sys.argv[1]):
            print('Game file is incomplete')
            sys.exit(1)
        else:
            game_info = GameInfo(sys.argv[1])
            game_board = GameBoard(game_info)
            game_board.set_visible(True)

