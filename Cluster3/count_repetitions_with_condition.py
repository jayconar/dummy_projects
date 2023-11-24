def count_consecutive_the(file_path):
    try:
        with open(file_path, 'r') as file:
            passage = file.read()
    except FileNotFoundError:
        return "File not found"

    words = passage.split()
    count = 0

    for i in range(len(words) - 2):
        if words[i].lower() == 'the' and 'the' in words[i + 2:] \
                and 'a' not in words[i + 1:words.index('the', i + 2)]:
            count += 1
    return f"The number of times 'the' is followed by another 'the' without 'a' in between: {count}"


print(count_consecutive_the('sample.txt'))

# Problem:
# Read a passage from a file.
# Count the number of times the word 'the' followed by another 'the' without 'a' in between.
#
# eg: The king went to the forest with the lady and a servant.
# The king shot a deer.
# The king went to the forest again the next day.
#
# answer is 4 (The king, the forest, The King the next).
