def pascals_triangle(rows):
    for i in range(rows):
        for j in range(rows - i - 1):
            print(" ", end=" ")
        for j in range(i + 1):
            print(binomial_coefficient(i, j), end=" "*3)
        print()


def binomial_coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


levels = 5
pascals_triangle(levels)

# Problem:
# Print the following pattern
#      1
#     1 1
#    1 2 1
#   1 3 3 1
#  1 4 6 4 1
#
# Observe how the numbers in the triangle are calculated.
