
with open("./Input/Letters/starting_letter.txt") as letter:
    content = letter.read()


with open("./Input/Names/invited_names.txt") as names:
    names_list = names.read().split('\n')
    for name in names_list:
        modified_content = content.replace("[name]", name)
        with open(f"./Output/ReadyToSend/{name}.txt", mode="w") as new_letter:
            new_letter.write(modified_content)


