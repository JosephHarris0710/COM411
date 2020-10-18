# Ask user to enter their name
print("What is your name human?")
name = input()
print("It is nice to meet you human", name)

# Read in user's name
name = input("What is your name human?")
#Commas compounds sentences and adds spaces
print("Nice to meet you human", name, ".")
#+ compounds sentences without spaces
print("Nice to meet you" + name + ".")
#.format using {} a more flexible varient
print("Nice to meet you {}.".format(name))