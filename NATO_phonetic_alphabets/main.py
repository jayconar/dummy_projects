import pandas
data = pandas.read_csv("NATO_phonetic_alphabet.csv")
ref_dict = {line.letter: line.code for (i, line) in data.iterrows()}


def generate():
    try:
        word = input("Type a word: ").upper()
        phonetic_alphabets = [ref_dict[letter] for letter in word]
        print(phonetic_alphabets)
    except KeyError:
        print("Please type alphabets only")
        generate()


generate()
