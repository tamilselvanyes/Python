# function with output

def multiply(a, b):
    return a*b


def format_name(first_name, last_name):
    # docstring
    """format the given first and last name"""
    return (f"{first_name.title()} {last_name.title()}")


print(format_name("tamil", "sElvan"))
