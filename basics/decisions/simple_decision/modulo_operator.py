number = int(input("Please enter a whole number: "))
modulo = number % 2
if (modulo == 1):
  print("The number {0} is an odd number".format(number))
else:
  print("The number {0} is an even number".format(number))
