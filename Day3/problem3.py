def summary(file_path):
    try:
        with open(file_path, 'r') as file:
            passage = file.read()

        words = passage.split()

        words = [str(''.join(char for char in word if char.isalpha())) for word in words]

        four_letter_words = [word.lower() for word in words if len(word) == 4]

        word_counts = {}
        for word in four_letter_words:
            word_counts[word] = word_counts.get(word, 0) + 1

        with open(file_path, 'a') as file:
            file.write("\n\nSummary of 4-letter words\n")
            for word, count in word_counts.items():
                file.write(f"{word}: {count} occurrences\n")

        print("Summary written to the file.")

    except FileNotFoundError:
        print("File not found")


summary('sample.txt')
