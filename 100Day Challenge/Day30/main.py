try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    print("Unable to open the file, Creating a file")
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key{error_message} does not exist")

else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")

height = float(input("Enter height in m"))
weight = int(input("Weight in kgs"))

if height > 3:
    raise TypeError("Human height can't be not more than 3")
