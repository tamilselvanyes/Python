with open("file1.txt") as first_file:
    first_list = first_file.readlines()
    list_one = [text.strip() for text in first_list ]

with open("file2.txt") as second_file:
    second_list = second_file.read().split('\n')
    list_two = [text.strip() for text in second_list ]

result = [num for num in list_one if num in list_two]

# Write your code above 👆

print(result)