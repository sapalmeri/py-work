"""
Classes ToDo
"""

# TODO: Section 1

# Create a class for an "Employee" that includes the instance attributes: "first_name", "last_name",
# "salary", and "title".


from turtle import color


class Employee:
  def __init__(self, first_name, last_name, salary, title):
    self.first_name = first_name
    self.last_name = last_name
    self.salary = salary
    self.title = title

  def printer(self):
    print(f"{self.first_name} {self.last_name} works as a {self.title} and makes ${self.salary} per year.")
    
p1 = Employee("Spongebob", "Squarepants", "50000", "Fry Cook")
    
p1.printer()

# Next, within the "Employee" class, create a method called "printer()" that prints the statement,
# "[first_name] [last_name] works as a [title] and makes $[salary] per year."
# IMPORTANT: Use f shorthand to fosrmat your print statement.



# Then, define a new instantion of "Employee" with "first_name" equal to "Spongebob", "last_name"
# equal to "Squarepants", "salary" equal to "50000" and "title" equal to "Fry Cook"



# Lastly, call the "printer()" method to print your formatted statement.



####################################################################################################

# TODO: Section 2

# Below is the class "SuperHero" with the instance attributes "name" and "powers". Within the class,
# write a method called "add_power()" that adds a new superpower to the "powers" list.

class SuperHero:
  def __init__(self, name):
    self.name = name
    self.powers = []

  # FIXME: Write your method here.

class SuperHero:
  def __init__(self, name):
    self.name = name
    self.powers = []
  
  def add_powers(self, powers):
    self.powers.append(powers)

superman = SuperHero("Superman")
superman.add_powers("heat vision")
superman.add_powers("superman strength")
superman.add_powers("invincibility")
print(superman.powers)

# Then, define a new instantiation of "SuperHero" with the "name" equal to "Superman" and store it
# in a variable called "super".



# Next, call the "add_power()" method three times to add the superpowers: "heat vision",
# "super strength", and "invincibility".



# Lastly, print the list of Superman's superpowers.


####################################################################################################

# TODO: Section 3

# Create a class named "Animal" with the instnace attributes "num_legs" and "weight".



# Then create a child class derived from "Animal" named "Mammal". Define the class attribute
# "habitat" equal to "land" for "Mammal". Define "species" and "color" as new instance attributes in
# the "Mammal" class.
# HINT: Use the "super()" function.


# Define a method in the "Mammal" class called "printer()" that prints the statement "The [species]
# is [weight] pounds and lives on [habitat]".



# Define an instantion of the "Mammal" class with "num_legs" eqaul to 4, "weight" equal to
# "700", "species" equal to "black bear", and "color" equal to "black" stored in the variable
# "bear".



# Lastly, call the "printer()" method.

class Animal:
  def __init__(self, num_legs, weight):
    self.num_legs = num_legs
    self.weight = weight

class Mammal(Animal):
  habitat = "land"
  def __init__(self, num_legs, weight, species, color):
    super().__init__(num_legs, weight)
    self.species = species
    self.color = color

  def printer(self):
    print(f"The species {self.species} is {self.weight} pounds and lives on {self.habitat}.")
          
bear = Mammal("4", "700", "black bear", "color")

bear.printer()





