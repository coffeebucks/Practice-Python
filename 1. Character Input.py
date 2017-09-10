name = input("Hey what is your name?").upper()
age = int(input("How old are you?"))
year_of_100 = str((2017 - age) + 100)
statement = (name + " will turn 100 years old in " + year_of_100 + '\n')
number = (int(input("How many times would you like this data to be printed?")))
print(statement * number)

"""Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)"""
