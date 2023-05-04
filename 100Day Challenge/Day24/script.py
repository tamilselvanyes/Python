

with open("my_file.txt", mode='w') as file:
    file.write("I was managed to change the content")


with open("my_file.txt", mode='a') as file:
    file.write("\n Appended a new line")

with open("my_file.txt") as file:
    content = file.read()
    print(content)