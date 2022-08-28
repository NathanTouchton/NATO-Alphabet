# from pandas import read_csv
import pandas

# TODO 1: Create a dictionary in this format:
# {"A": "Alpha", "B": Bravo}

data = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter:row.code for (index, row) in data.iterrows()}

# TODO 2: Create a list of phonetic code words from word user inputs

user_word = input("Pick a word to translate into NATO alphabet: ").upper()

def generate_nato_list(word):
    try:
        nato_list = [alphabet_dict[letter] for letter in word]

    except KeyError:
        print("Sorry, please enter only letters.")
        user_word = input("Pick a word to translate into NATO alphabet: ").upper()
        generate_nato_list(user_word)

    else:
        print(nato_list)

generate_nato_list(user_word)
