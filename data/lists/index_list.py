def movements():
  path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
  return path

def run():
  print("Moving...")
  path = movements()

  for x in range(4):
    print(path[2*x],"for",path[2*x+1],"steps")

run()