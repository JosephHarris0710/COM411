first_number = int(input("Please enter the first whole number:"))
second_number = int(input("Please enter the second whole number:"))
third_number = int(input("Please enter the third whole number:"))

even_count = 0

first_modulo = first_number % 2
if (first_modulo == 0):
  even_count = even_count + 1

second_modulo = second_number % 2
if (second_modulo == 0):
  even_count = even_count + 1

third_modulo = third_number % 2
if (third_modulo == 0):
  even_count = even_count + 1
  
odd_count = 3 - even_count

print("There were {0} even numbers and {1} odd numbers".format(even_count,odd_count))