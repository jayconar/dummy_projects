sequence = "a"

for char in range(ord('a'), ord('h')):  # Up to and including 'g'
    print(sequence)
    sequence = sequence + chr(char + 1) + sequence

# Output:
# a
# aba
# abacaba
# abacabadabacaba
# abacabadabacabaeabacabadabacaba
# abacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacaba
# abacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacabagabacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacaba
