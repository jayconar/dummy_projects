def process_text(text):
    """Removes punctuation and converts to lowercase"""
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    for char in punctuation:
        text = text.replace(char, "")
    text = text.lower()
    return text


def count_words(text):
    """Creates and returns a dictionary with each unique word and its occurrences"""
    words = text.split()
    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1
    return word_counts


def main():
    essay = input("Type the file location:\n")
    # Reads the essay from the specified file
    with open(essay, "r") as file:
        essay_text = file.read()

    cleaned_text = process_text(essay_text)
    word_counts = count_words(cleaned_text)
    print(word_counts)


main()

# Output:
# Type the file location: C:\Users\Subhash\Documents\essay.txt
# {'burgundy': 10, 'is': 7, 'a': 5, 'region': 2, 'famous': 1, 'for': 1, 'its': 3, 'wine': 5, 'the': 5, 'word': 1,
# 'evokes': 1, 'vineyards': 1, 'hills': 1, 'and': 12, 'villages': 2, 'in': 1, 'winemaking': 1, 'an': 1, 'art': 1,
# 'pinot': 1, 'noir': 1, 'chardonnay': 1, 'grapes': 1, 'produce': 1, 'fine': 1, 'wines': 3, 'have': 2, 'rich': 1,
# 'flavors': 1, 'deep': 1, 'color': 1, 'velvety': 1, 'hue': 1, 'enchanting': 1, 'it': 2, 'signifies': 1, 'elegance': 1,
# 'isnt': 1, 'just': 1, 'history': 3, 'culture': 1, 'dijon': 1, 'capital': 1, 'city': 1, 'has': 2, 'heritage': 1,
# 'burgundian': 1, 'cuisine': 1, 'delightful': 1, 'coq': 1, 'au': 1, 'vin': 1, 'boeuf': 1, 'bourguignon': 1,
# 'are': 1, 'tasty': 1, 'pair': 1, 'them': 1, 'with': 2, 'glass': 2, 'of': 1, 'burgundys': 2, 'like': 1, 'beaune': 1,
# 'pommard': 1, 'nuitssaintgeorges': 1, 'old': 2, 'wineries': 1, 'climate': 1, 'crucial': 1, 'cold': 1, 'winters': 1,
# 'warm': 1, 'summers': 1, 'blends': 1, 'tradition': 1, 'innovation': 1, 'winemakers': 1, 'use': 1, 'modern': 1,
# 'techniques': 1, 'while': 1, 'respecting': 1, 'methods': 1, 'visiting': 1, 'journey': 1, 'into': 1, 'beauty': 1,
# 'flavor': 1, 'captivates': 1, 'enthusiasts': 1, 'travelers': 1, 'raise': 1, 'your': 1, 'to': 1, 'place': 1, 'that': 1,
# 'charms': 1, 'wonders': 1}
