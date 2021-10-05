#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Create empty list to store items that will make up the password
letter = []
number =[]
symbol = []

#use for loops to randomly select items from each list based on the users input
for letter in letters:
  letter = random.sample(letters,nr_letters)

for number in numbers:
  number = random.sample(numbers,nr_numbers)

for symbol in symbols:
  symbol = random.sample(symbols,nr_symbols)

#Concatenate the list and store in a variable
password = letter + symbol + number

# Randomize the items of the new list
random.shuffle(password)

print(password)

# Change to string
password_new = " "
for char in password:
  password_new += char

print(password_new)
