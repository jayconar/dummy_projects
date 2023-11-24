def encode(input_text, encode_key):
    words = input_text.split()
    encoded_words = []
    position = 1

    def wrap_char(char, key):
        """Function that handles shifting and wrapping characters"""
        if 'a' <= char <= 'z':
            # Lowercase alphabet
            return chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            # Uppercase alphabet
            return chr(((ord(char) - ord('A') + key) % 26) + ord('A'))
        else:
            # Special characters and numbers remain unchanged
            return char

    for word in words:
        """Iterates through the words and encodes words at odd and even positions accordingly"""
        if position % 2 == 0:
            # Reversing the word at even positions and encoding
            reversed_word = word[::-1]
            encoded_word = "".join(wrap_char(char, encode_key) for char in reversed_word)
            encoded_words.append(encoded_word)
        else:
            # Shifting each key by the shift key without modifying the word
            encoded_word = "".join(wrap_char(char, encode_key) for char in word)
            encoded_words.append(encoded_word)

        position += 1

    # Converting the encoded_words list into a single string
    final_text = ' '.join(encoded_words)

    return final_text


text = input("Type the word you want to encode:\n")
shift_number = int(input("Type the encode key: "))
encoded_text = encode(text, shift_number)
print(f"Encoded Text: {encoded_text}")

# Output:
# Type the word you want to encode:
# This is water.
# Type the encode key: 4
# Encoded Text: Xlmw wm aexiv.

# Retains numbers and special characters
# Retains uppercase and lowercase letters
