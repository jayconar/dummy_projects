sequence = 'a'

for char in range(ord('a'), ord('h')):  # Up to and including 'g'
    print(sequence)
    sequence = sequence + chr(char + 1) + sequence

# Problem:
# Generate the following pattern using for loop. Go up to g.
# a
# aba
# abacaba
# abacabadabacaba
# abacabadabacabaeabacabadabacaba
