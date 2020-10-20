def directions():
  return ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]

def menu():
  print("Please select a direction:")
  options = directions()
  for x in range(len(options)):
    print("{}: {}".format(x, options[x]))
  choice = int(input())
  return options[choice]

def run():
  route = []
  print("Working out escape route...")
  for x in range(5):
    route.append(menu())
  print("Escape route: {}".format(route))

run()