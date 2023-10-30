from enum import Enum
import numpy as np

BOARD_COLS = 7
BOARD_ROWS = 6
BOARD_SHAPE = (6,7)
INDEX_HIGHEST_ROW = BOARD_ROWS - 1 
INDEX_LOWEST_ROW = 0

BoardPiece = np.int8
NO_PLAYER = BoardPiece(0)
PLAYER1 = BoardPiece(1)
PLAYER2 = BoardPiece(2)

BoardPiecePrint = str
NO_PLAYER_PRINT = BoardPiecePrint(' ')
PLAYER1_PRINT = BoardPiecePrint('X')
PLAYER2_PRINT = BoardPiecePrint('O')

PlayerAction = np.int8

class GameState(Enum):
    IS_WIN = 1
    IS_DRAW = -1
    STILL_PLAYING = 0

def initialize_game_state() -> np.ndarray:
      """
    Returns an ndarray, shape BOARD_SHAPE and data type (dtype) BoardPiece, initialized to 0 (NO_PLAYER).
    """
    raise NotImplementedError

def pretty_print_board(board: np.ndarray) -> str:
    """
    Should return `board` converted to a human readable string representation,
    to be used when playing or printing diagnostics to the console (stdout). The piece in
    board[0, 0] of the array should appear in the lower-left in the printed string representation. Here's an example output, note that we use
    PLAYER1_Print to represent PLAYER1 and PLAYER2_Print to represent PLAYER2):
    |==============|
    |              |
    |              |
    |    X X       |
    |    O X X     |
    |  O X O O     |
    |  O O X X     |
    |==============|
    |0 1 2 3 4 5 6 |
    """
    raise NotImplementedError()