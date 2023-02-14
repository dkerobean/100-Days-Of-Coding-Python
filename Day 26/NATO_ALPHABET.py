import pandas

alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in alphabet_data.iterrows()}

user_word = input("Enter a word: ").upper()

output_list = [phonetic_dict[letter] for letter in user_word]

print(output_list)
