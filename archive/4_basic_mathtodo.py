"""
Lets calculate a company's taxes, profit, and then divide the profit amongst shareholders.
"""

# TODO: Section 1:
# TIP: Use print statements to test your code along the way.

# Set the following variables and constants:
# Set a constant of "TAX_RATE" equal to .20 (we will use this as twenty percent).

# Receive a user input for the question "What was your revenue for this year?". Set
# the input equal to a variable called "revenue".
# HINT: What varible type do you want "revenue" to be?

# Set a variable equal to "taxes_paid". Calculate the taxes by multipling the rate (20%)
# from your previous variable by the revenue input from the user.

# Set a new variable called "profit". Calculate the revenue minus the taxes paid and set it
# equal to this variable.

# In this lesson we went over changing the value of a variable. In this example, your company
# is taking a one time charge of 50%. This is done by executing the following:
# profit = profit / 2 #IMPORTANT: Uncomment this line before moving on.

TAX_RATE = .20
revenue = float(input("What was your revenue for this year?"))
taxes_paid = TAX_RATE * revenue
profit = revenue - taxes_paid
profit = profit / 2
print(profit)


# TODO: Section 1.1:
# Print an output indicating "Company ____ recorded $______  in revenue this year,
# paid $______ in taxes, recorded a profit of $______, and paid $______ to their five
# shareholders, evenly". Be sure to format to look like normal dollar amounts - "$xx.xx"

print("Company Shane recorded $10000.00 in revenue this year, paid $2000.00 in taxes, recorded a profit of $4000.00, and paid $800.00 to their five shareholders, evenly.")

# TAKEAWAY:
# 1) Variables that have input functions stored in them will be of the string type. To use them in
#    math operations, you must convert them to an integer or float.
# 2) You can alter the value of a variable by setting it equal to an operation on itself.
#    example: x = x * 2.

####################################################################################################

# TODO: Section 2:
num_list = [35, 4, 20, 100, 96]
# Set the minimum, maximum, and sum of num_list to the variables "min_num", "max_num", and
# "sum_list" respectively. Then print each in their own print statement in the format
# "The ___ of num_list is ___." using f shorthand.

min_num = min(num_list)
print(f"The min of num_list is {min_num}.")

max_num = max(num_list)
print(f"The max of num_list is {max_num}.")

sum_list = sum(num_list)
print(f"The sum of num_list is {sum_list}.")

# TODO: Section 2.1:
num_list2 = [-20, 15, -27, -11]
# Find the sum of num_list2 and store it in the variable "sum2". Then print the sum in the format,
# "The sum is ___". Then using f shorthand, return the value of the absolute value of "sum2" and
# print in the format, "The absolute value of sum2 is ___".

sum2 = sum(num_list2)
print(f"The sum is {sum2}.")
abs_neg = abs(-43)
print(f"The asbolute value of sum2 is {abs_neg}.")