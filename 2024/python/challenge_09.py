from typing import List, Literal

# fmt: off
board = [
  '·····',
  '*····',
  '@····',
  'o····',
  'o····'
]
# fmt: on


def move_train(
    board: List[str], mov: Literal["U", "D", "R", "L"]
) -> Literal["none", "crash", "eat"]:
    # Update board to a useful matrix
    board = [[char for char in line] for line in board]
    height = len(board)
    width = len(board[0])

    # Find train initial position
    train_row = 0
    train_col = 0
    for row in range(height):
        for col in range(width):
            if board[row][col] == "@":
                train_row = row
                train_col = col

    match mov:
        case "U":
            if train_row - 1 < 0:
                return "crash"

            char = board[train_row - 1][train_col]
            if char == "*":
                return "eat"
            elif char == "o":
                return "crash"
        case "D":
            if train_row + 1 >= height:
                return "crash"

            char = board[train_row + 1][train_col]
            if char == "*":
                return "eat"
            elif char == "o":
                return "crash"
        case "L":
            if train_col - 1 < 0:
                return "crash"

            char = board[train_row][train_col - 1]
            if char == "*":
                return "eat"
            elif char == "o":
                return "crash"
        case "R":
            if train_col + 1 >= width:
                return "crash"

            char = board[train_row][train_col + 1]
            if char == "*":
                return "eat"
            elif char == "o":
                return "crash"

    return "none"
