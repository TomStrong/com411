def likelihood():
  return (50, 38, 27, 99, 4)

def run():
  chance = likelihood()
  print("Minimum likelihood of falling: {}%".format(min(chance)))

run()