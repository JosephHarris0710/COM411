#str is used to allocate the string data type
name = str(input("What is your name human: "))
#int is used to allocate the integer data type
age = int(input("How old are you (in years): "))
#float is used to allocate the decimal data type
height = float(input("How tall are you (in meters): "))
weight = float(input("How much do you weigh (in kilograms): "))

bmi = float(weight / height**2)
formated_bmi = "{:0.2f}".format(bmi)

print("{0} you are {1} years old and your bmi is {2}".format(name,age,formated_bmi))