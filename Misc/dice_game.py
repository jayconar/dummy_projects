import random

# Initializing the game board as a 6x6 grid of '*'
board = [['*' for _ in range(6)] for _ in range(6)]

# Initializing player scores
player_A_score = 0
player_B_score = 0

# Defining the players' initials
player_A = 'A'
player_B = 'B'

# Main game loop
while player_A_score < 5 and player_B_score < 5:
    # Player A's turn
    print("Player A's turn:")
    input("Press Enter to roll the dice...")
    row_A = random.randint(1, 6)
    col_A = random.randint(1, 6)
    print(f"Player A rolled: ({row_A}, {col_A})")

    if board[row_A - 1][col_A - 1] == player_B:
        player_A_score += 1

    board[row_A - 1][col_A - 1] = player_A
    print("Updated Game Board:")
    for row in board:
        print(' '.join(row))
    print(f"Player A's Score: {player_A_score}")
    print(f"Player B's Score: {player_B_score}")

    # Checking if Player A has won
    if player_A_score == 5:
        print("Player A wins!")
        break

    # Player B's turn
    print("Player B's turn:")
    input("Press Enter to roll the dice...")
    row_B = random.randint(1, 6)
    col_B = random.randint(1, 6)
    print(f"Player B rolled: ({row_B}, {col_B})")

    if board[row_B - 1][col_B - 1] == player_A:
        player_B_score += 1

    board[row_B - 1][col_B - 1] = player_B
    print("Updated Game Board:")
    for row in board:
        print(' '.join(row))
    print(f"Player A's Score: {player_A_score}")
    print(f"Player B's Score: {player_B_score}")

    # Checking if Player B has won
    if player_B_score == 5:
        print("Player B wins!")

# End of the game
print("Game Over!")
