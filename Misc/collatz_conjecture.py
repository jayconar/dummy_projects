# Program to compare the number of steps in collatz conjecture for any two positive integers

number_1 = int(input("Type the first number: "))
number_2 = int(input("Type the second number: "))


def collatz(number):
    """Performs operations accordingly until it reaches 1"""
    step = []
    while number != 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = 3 * number + 1
        step.append(number)
    return step


if len(collatz(number_2)) > len(collatz(number_1)):
    print(f"{number_1} has less steps, i.e., {len(collatz(number_1))} steps")
elif len(collatz(number_1)) > len(collatz(number_2)):
    print(f"{number_2} has less steps, i.e., {len(collatz(number_2))} steps")
else:
    print(f"Both {number_1} and {number_2} have {len(collatz(number_2))} steps")

# Output
# Type the first number: 13
# Type the second number: 12
# Both 13 and 12 have 9 steps

# print(f"{collatz(number_1)}\n{collatz(number_2)}")
# [40, 20.0, 10.0, 5.0, 16.0, 8.0, 4.0, 2.0, 1.0]
# [6.0, 3.0, 10.0, 5.0, 16.0, 8.0, 4.0, 2.0, 1.0]
