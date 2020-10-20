def directions():
  return ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]

def menu():
  print("Please select a direction:")
  options = directions()
  for x in range(len(options)):
    print("{}: {}".format(x, options[x]))

def run():
  menu()

run()