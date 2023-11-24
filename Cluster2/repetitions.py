def count_repetitions(text):
    words = text.split()
    consecutive_count = 0

    for i in range(len(words) - 1):
        if words[i] == words[i + 1]:
            consecutive_count += 1

    return consecutive_count


passage = "The quick brown fox jumped over the lazy lazy lazy dog. The dog didn't notice the fox. " \
          "The fox, however, noticed the lazy lazy dog and decided to jump over it again. " \
          "It was an interesting sight to see the lazy lazy dog and the quick quick fox in action."
print(count_repetitions(passage))

# Problems:
# Write a program that reads a passage or string and counts the occurrences of two consecutive words
# that are the same without any other word in between.
# For example, count the occurrences of "apple apple" but not "apple orange apple."
