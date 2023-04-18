alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceaser(text, shift, direction):
    cipher_text = ""
    if (direction == "decode"):
        shift *= -1
    for letter in text:
        if (letter not in alphabet):
            cipher_text += letter
        else:
            cipher_text += alphabet[(alphabet.index(letter) + shift) % 26]
    print(f"Your {direction}d word is {cipher_text}")


def execute():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(text, shift, direction)
    repeat()


def repeat():
    try_again = input("Type 'yes' if you wanna go again or 'no' to exit \n")
    if (try_again == "yes"):
        execute()
    elif (try_again == "no"):
        print("Thank you")
    else:
        print("Invalid input")
        repeat()


print("Welcome to Caesar Cipher System, We value your message none of it saved with us.\n\n")
execute()
