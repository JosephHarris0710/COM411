def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left","Turn Right"]
  return directions

def menu():
  print("Please select a direction:")
  direction = directions()
  for x in range(len(direction)):
    print("{}:{}".format(x,direction[x]))

def run():
  menu()

run()