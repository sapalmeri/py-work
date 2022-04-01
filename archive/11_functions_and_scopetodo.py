"""
Working with functions and scope
"""

# TODO: Section 1
# Define a function called "double()" that sets a parameter of "x". The function should double "x"
# and print the product. Call the function and pass it the below variable as an argument.

double_this = 7
x = double_this
def double(x):
    new_double = x * 2
    print(new_double)
double(7)

def printer():
    print(double_this)
printer()


# After completing the above, define a function called "printer()" that sets no parameter.
# The function should just print the "double_this" variable. Then call the function.

####################################################################################################

# TODO: Section 2
# Copy your "double()" function from above to this block of code. Change the function to use a
# return value, store that return value in a variable, and print the product.

double_this = 38
x = double_this
def double(x):
    new_double = x * 2
    return new_double
print(double(x))

####################################################################################################

# TODO: Section 3
# Write a function that takes an input statement of an integer and store it in a variable called
# "num". and then tests if the integer is even or odd. If the input is even, print "[num] is even."
# Otherwise print the statement "[num] is odd." Lastly call the function.
num = int(input("Enter any Number: "))
def eoro(num):
    new_num = num % 2
    if new_num == 0:
        print(num, "is even.")
    else:
        print(num, "is odd.")
eoro(num)

####################################################################################################

# TODO: Section 4
# Define a function that takes a dictionary as a parameter, loops through the dictionary, and
# returns the iteration number, key, and value in the following format:
# "Iteration number [1] returns the key [key] and the value [value]." Lastly call the function.

# Here is an example dictionary:

EXAMPLE_DICTIONARY = {"key_one": "value_one", "key_two": "value_two", "key_three": "value_three", "key_four": "value_four"}
def dictionary_reader(EXAMPLE_DICTIONARY):
    i = 0 
    for key in EXAMPLE_DICTIONARY:
        value = EXAMPLE_DICTIONARY[key]
        i += 1
        print(f"Iteration number {i} returns the key {key} and the value {value}.")
dictionary_reader(EXAMPLE_DICTIONARY)
   
