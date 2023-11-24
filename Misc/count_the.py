# Opening the file for reading
with open("input.txt", "r") as file:
    # Reading the contents of the file and storing it in a variable
    text = file.read()
# Splitting the text into sentences (assuming the text is punctuated)
sentences = text.split(". ")

# Initializing a variable to keep track of the count
count = 0

# Iterating through each sentence
for sentence in sentences:
    words = sentence.split()
    # Iterate through each word in the sentence
    for i in range(len(words) - 1):
        if words[i].lower() == 'the' and words[i + 1].lower() == 'the':
            # Check if there's no 'a' in between
            if 'a' not in words[i:i + 2]:
                count += 1

# Printing the count
print(f"The count of 'the the' without 'a' in between is: {count}")
