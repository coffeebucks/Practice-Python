"""Ask the user for a number. 
Depending on whether the number is even or odd, print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?
"""


#MY SOLUTIONS

number = int(input("Can you guess my number?"))
if number % 4 == 0:
  print("Bingo! You have some superpower or something?")
elif number % 2 == 0:
  print("Not there yet but good direction. Now you know that number is an even.")
else:
  print("Oopsy! hmmm?")
  
"""EXTRAS
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. If not, print a different appropriate message."""

#MY SOLUTIONS

num = int(input("Please give me a number again:"))
check = int(input("Please give me another number:"))
if num % check == 0:
  print(str(num) + " can be divideded evenly by " + str(check))
else:
  print("They should be divided evenly.")
  
  
