import random


def roll_dice():
    return random.randint(1, 6)


def print_board(board):
    for row in board:
        print(' '.join(row))
    print()


def update_board(board, player, row, col, scores):
    if board[row][col] == '*':
        board[row][col] = player
    else:
        scores[player] += 1
        board[row][col] = player


def game():
    board = [['*' for _ in range(6)] for _ in range(6)]
    scores = {'A': 0, 'B': 0}

    while scores['A'] < 5 and scores['B'] < 5:
        input("Player A, press Enter to roll the dice...")
        row_a, col_a = roll_dice(), roll_dice()
        update_board(board, 'A', row_a - 1, col_a - 1, scores)
        print_board(board)
        print(f"You rolled: {row_a}  {col_a}\nScore: Player A - {scores['A']}, Player B - {scores['B']}\n")

        input("Player B, press Enter to roll the dice...")
        row_b, col_b = roll_dice(), roll_dice()
        update_board(board, 'B', row_b - 1, col_b - 1, scores)
        print_board(board)
        print(f"You rolled: {row_b}  {col_b}\nScore: Player A - {scores['A']}, Player B - {scores['B']}\n")

    result = "It's a draw, Nobody" if scores['A'] == scores['B'] else ('Player B' if scores['B'] == 5 else 'Player A')
    print(f'{result} wins')


if __name__ == "__main__":
    game()

# Question:
# You have 6 x 6 game board where each cell is shown as a *
# This is a two player dice game. The die has numbers 1 to 6.
# Each player rolls the dice twice. First roll is row number, second roll is col number.
# After the player rolls the dice, in the (row,col) enter the player's initial.
# If the player  A rolls the dice and  if  player B already has their initial in the same row,col
# Add a point to A and change the initial to A.
#
# Player who gets 5 points first wins the game.
# Print the board each time after the user rolls and also print the current score.
