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
