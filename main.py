# This is a simple calculator program.
# Written by: Thu Aung
# Written on: Dec 10, 2020.

print("Welcome to the Calculator Program.")
print("The numbers to be used in selected program must be entered with a space between them.")
print("For Division and Power, just two numbers can be provided.\n")

# Get user to select a program to use.
choice = input("Type\n1 for Multiplication\n2 for Division\n3 for Addition\n4 for Subtraction\n5 for Power.\n")
print(f"The user choice is: {choice}")

# Get the numbers a user wants to use in a selected program.
number = input("Type in the number with space between them. ").split()
# Change all user's input as integers to do calculations.
for i in range(0, len(number)):
  number[i] = int(number[i])

def multiplication():
  # Total must start at 1 for multiplication to work. If it started as 0, all multiplications would result as 0.
  total = 1
  for num in number:
    total *= num
  print("The multiplication of the numbers you provided is: ", total)

def division():
  total = 0
  for i in range(0,len(number)-1):
    total = number[i]/ number[i+1]
  print(f"The division of the numbers you provided is: {total:.2f}")

def addition():
  total = 0
  for num in number:
    total += num
  print(f"The addition of the numbers you provided is: {total}")

def subtraction():
  # Total must be the first number entered.
  total = number[0]
  for num in range(1, len(number)):
    total -= number[num]
  print(total)

def power():
  total = 0
  for i in range(0, len(number)-1):
    total = number[i] ** number[i+1]
  print(f"The power of the numbers you provided is: {total}")

if choice == '1':
  multiplication()
elif choice == '2':
  if len(number) > 2:
    print("Error: Just Two numbers can be entered.")
  else:
    division()
elif choice == '3':
  addition()
elif choice == '4':
  subtraction()
elif choice == '5':
  if len(number) > 2:
    print("Error: Just Two numbers can be entered.")
  else:
    power()
else: 
  print("Invalid entry.")




