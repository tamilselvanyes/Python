# test program
def mystery(s):
    if (len(s) == 1):
        return s
    return mystery(s[1:]) + s[0]


# print(mystery("python"))


# dictionaries
# {key:value}


dictionary_example = {
    "key1": "value1",
    "key2": "value2"
}

empty_dictionary = {}

# adding a new property to the dictionary
dictionary_example["key3"] = "value3"

# edit an item in the dictionary
dictionary_example["key1"] = "value4"


# print(dictionary_example["key1"])
# wiping a dictionary
# dictionary_example = {}

# print(dictionary_example)


# looping through a dictinary
for property in dictionary_example:
    print(property)

for property in dictionary_example:
    print(dictionary_example[property])
