# calling price for products using DICT and Conditionals.
# Grocesries 

fruit_list = {'expired banana': 2.99, 'devil lemon': 3, 'crazy bacon': 1.99}

print('Welcome to Woolworths! Today we have the following fruits on special!')
for fruit in fruit_list:
  print(fruit)

print('What would you like today?')

choice = input()
if choice in fruit_list:
  print ('{} is {} dollors!'.format(choice, fruit_list[choice]))
else:
  print ('Sorry, but seriously {} is out of stock.'.format(choice))
  
