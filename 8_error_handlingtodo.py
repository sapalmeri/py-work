"""
Lets clean up some errors
"""


# TODO: Section 1.1:

# Run the code below to find what type of error you are encountering. Then comment out the code and
# rewrite it with a new denominator to fix the error. Then print the type of error you got from the
# original problem.

# number = 10 * (1/0) # FIXME

number = 10 * (1/2)
print(ZeroDivisionError)

# TODO: Section 1.2:
# Again, run the code below to find what type of error you are encountering. Then define 'spam' on
# the correct line and print the error type you originally received.

# equation = 4 + spam * 3 # FIXME
spam = 2
equation = 4 + spam * 3
print(NameError)


# TODO: Section 1.3:
# Finally, run the code below to find what type of error you are encountering. Change the code so that
# our '2 + 2' addition works and print the error type you originally received.

# twotwo = '2' + 2 # FIXME
two = int('2')
twotwo = two + 2
print(TypeError)

