# day 2 datatypes string,integer,float,boolean.
# subscripting
print("Hello"[0])
string_type = "string"


# interger
# below is 34 thousands as the compiler will remove
# underscore and consider it to be whole
numone = 34_234
numtwo = 235
float_one = float(numone)

# print(numone + numtwo+float_one)
converted_num = str(numone)

booleanValue = False
# print(type(booleanValue), type(numone), type(string_type), type(converted_num))


# Arithmetic opetation order PEDMAS (left to right)
# p-parentheses ()
# exponent **
#  multiplication,division * /
# addition,subtraction +,l


# f-string implementation
print(f"your string is {booleanValue}{numone}")
