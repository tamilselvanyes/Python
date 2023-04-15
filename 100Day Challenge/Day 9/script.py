# dictionaries


# test program
def mystery(s):
    if (len(s) == 1):
        return s
    return mystery(s[1:]) + s[0]


print(mystery("python"))
