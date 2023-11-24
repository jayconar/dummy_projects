import random


def roll_dice():
    return random.randint(0, 5)


def play_game():
    points = 0

    while points < 50:
        input("Press any key to roll the dice")
        roll_result = roll_dice()

        if roll_result == 0:
            print("Oops! You rolled a 0. Game Over!")
            break
        elif roll_result % 2 == 0:
            points += 2
            print(f"You rolled {roll_result}. You gained 2 points. Total points: {points}")
        elif roll_result in [1, 3]:
            print(f"Jump! It's a {roll_result}")
        elif roll_result == 5:
            points += 3
            print(f"You rolled a 5. You gained 3 points. Total points: {points}")

    if points >= 50:
        print(f"Congratulations! You reached 50 points and won the game!")


play_game()
