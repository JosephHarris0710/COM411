booktype = str(input("Is the book soft or hard cover? "))
perfect_bound = str(input("Is the book perfect bound? "))

if (booktype == "soft"):
  if (perfect_bound == "yes"):
    print("Soft cover, perfect bound books are very popular!")
  else:
    print("Soft covers with coils or stitches are great for short books")
elif (booktype == "hard"):
  print("Books with hard covers can be more expensive!")