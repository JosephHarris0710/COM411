first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))

if (first_number < second_number):
  print("The first number is the smallest")
elif (first_number > second_number):
  print("The second number is the smallest")
elif (first_number == second_number):
  print("Both are equal!")
else:
  print("Error")