def movements():
  path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
  return path

def run():
  print("Moving...")
  path = movements()

  for x in range(len(path)):
    if ((x - 1) % 2 == 0):
      print("{} for {} steps".format(path[x-1], path[x]))

run()