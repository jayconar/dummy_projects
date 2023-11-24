def reverse(passage):
    words = passage.split()
    reversed_words = [word[::-1] for word in words]
    reversed_passage = ' '.join(reversed_words)
    return reversed_passage


sentence = input("Enter a passage: ")
print("Reversed Passage:", reverse(sentence))
