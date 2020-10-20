def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu():
  print("Please select a direction:")
  direction = directions()
  for x in range(len(direction)):
    print("{0}:{1}".format(x,direction[x]))
  choice = int(input())
  return direction[choice]

def run():
  route = []
  print("Working out escape route...")
  for x in range(5):
    choice = menu()
    route.append(choice)
  print("Escape Route: {}".format(route))

run()