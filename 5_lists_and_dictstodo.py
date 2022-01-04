"""
Working with lists, dictionaries, and nested data
"""

# TODO: Section 1.1:
# Identifying index values[]

greek_letters = ["Alpha", "Beta", "Gamma"]
# Save the item in the list, "greek_letters" that is equal to index value "0" as a variable, then
# print the variable.

greek_letters[0] = "Alpha"
print(greek_letters[0])

# TODO: Section 1.2:
# In a variable called "last_item", store the last item of "greek_letters" using the index value of
# -1. Then print "last_item".

last_item = greek_letters[-1]
print(last_item)

# TODO: Section 1.3:
# Add the word "Delta" to the list "greek_letters". Using the index value of -1 again, store the
# last item of "greek_letters" in a variable called "last_item" and print it.
# IMPORTANT: Remember you can reassign values to variables.

greek_letters.append("Delta")
last_item = greek_letters[-1]
print(last_item)

####################################################################################################

# TODO: Section 2:
# Combining concepts of lists and dictionaries
DAYS_OF_WEEK = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# In the following dictionary, the keys are associated with days of the week (i.e. Sunday = 0) and
# the values represent temperatures. Dictionaries have indexes just like lists do.
temperature_forecast = {"0": 85, "1": 70, "2": 80, "3": 72, "4": 67, "5": 95, "6": 100}

# Print out "Wednesday" with it's index value from the list "DAYS_OF_WEEK". Set that value equal
# to a variable called "weds".

# Print Wednesday's temperature by using the forecast dictionary.

print(DAYS_OF_WEEK[3])
weds = 3
temperature_forecast[3] = 72
print(temperature_forecast[3])

# Use the variable "weds" directly in the print statement below, but for the temperature
# access the value directly in the print statement.
# Your output should read "The temperature on Wednesday will be 72 degrees." Be sure to use
# f shorthand!

####################################################################################################

# TODO: Section 3:
# To begin, set the first student of the math class to a variable called "first_student".
# Next, set the english class' starting time to a variable called "english_start".
# Lastly, print each in separate print statements.
classes = [
    {
        'subject': 'math',
        'level': 'linear algebra',
        'students': ['billy', 'beatrice', 'bronny', 'bart'],
        'teacher_description': {
            'name': 'Betty',
            'education': ['Masters of Math', 'Bachelors of Science']
        },
        'classTime': ['11:00 AM', '12:30 PM']
    },
    {
        'subject': 'english',
        'level': 'composition',
        'students': ['chris', 'callie', 'crysta', 'calista'],
        'teacher_description': {
            'name': 'Joanny',
            'education': ['PHD of English', 'Masters of Literacy', 'Bachelors of Biology']
        },
        'classTime': ['1:00 PM', '2:45 PM']
    }
]

math = classes[0]
english = classes [1]
first_student = math['students'][0]
english_start = english['classTime'][0]
print(first_student)
print(english_start)

