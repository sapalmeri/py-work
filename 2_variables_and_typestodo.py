"""
Using variables and types
"""

# TODO: Section 1:
# Set a variable 'phrase1' euqal to "Hi everyone! " and another variable 'phrase2'
# equal to "My name is [name here]". Then use what you learned so
# far in the lesson to set these varibles to a new variable called "complete"
# and print it.

from ctypes.wintypes import SC_HANDLE

phrase1 = "Hi everyone! "
phrase2 = "My name is Shane."
complete = phrase1 + phrase2
print(complete)
####################################################################################################

# TODO: Section 2:
# Set two variable in the same line, "flt1" and "flt2", equal to 3.5 and 14.0, respectively.
# Then print each variable to check the output.

flt1, flt2 = 3.5, 14.0
print(flt1, flt2)

####################################################################################################

# TODO: Section 3:
# Set a variable called name equal to your name, then set a variable of age
# equal to your age as an integer. Print a statement with an output of
# "My name is [name here] and I am [age here] years old." using the above
# variables in your print statement.

name = "Shane"
age = 19
print("My name is", name, "and I am", age, "years old.")

# Takeaway:
# Concatenation (+) can only be done with strings, not strings and integers/floats. Commas, however,
# simply print different elements rather than attempting to concatenate strings.

####################################################################################################

# TODO: Section 4:
# Set a variable equal to each of the types we have learned so far. That includes
# integers, floats, booleans, None, and strings. So, have one variable per each
# of those types (i.e. exampleInt = 0, exampleBool = False, etc.).
# To check the type of something in python, you use the type() function.
# For example, type("Hello") would yield string, and type(6) would yield int.
# So, create on print statement that would print the type of each variable you've set.

int1, flt1, bool1, str1 = 5, 14.5, True, "hi"
print("int1:", type(int1))
print("flt1:", type(flt1))
print("bool1:", type(bool1))
print("str1:", type(str1))


# Takeaway:
# Types are important in Python and you can check different elements' types using type().
# The type() function is an example of a polymorphic function, meaning that the same
# function name can be used for different types.

####################################################################################################

# TODO: Section 5:

# Lastly, we will introduce type conversion. There are functions you can use to
# convert things in Python. The first type conversion function we will use is str().
# Try the problem from Section 3, but use plus signs to concatenate strings and
# print "My name is [name here] and I am [age here] years old." using the name and age
# variables. However, this time when you're concatenating the age variable, wrap it in the
# str() function as such: str(age). The print statement will no longer throw an
# error ???? since age was converted to a string.

name = "Shane"
age = "19"
print("My name is " + name + " and I am " + str(age) + " years old.")

# Takeaway:
# We can change types in Python when appropriate, and we learned one way to do so with str()

# Good job, everyone! First todo down ????????
