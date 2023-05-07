student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

df = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row["letter"]: row["code"] for (index, row) in df.iterrows()}

game_is_on = True

while game_is_on:
    user_input = input("Please enter the word").upper()
    letters = user_input.split()

    if user_input == "EXIT":
        game_is_on = False
    else:
        phonetic_words = [data_dict[letter] for letter in user_input]
        print(phonetic_words)
