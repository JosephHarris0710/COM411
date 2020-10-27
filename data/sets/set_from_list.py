def observed():
  observations = []
  for x in range(7):
    observations.append(input("Please enter and observation:"))
  return observations

def run():
  observations = observed()
  observed_set = set()

  print("Counting observtions...")
  for observation in observations:
    occurences = observations.count(observation)
    observed_set.add((observation, occurences))

  for items, value in observed_set:
    print("{items} observed {value} times.".format(items,value))

run()