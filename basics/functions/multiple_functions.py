def display_ladder(steps):
  for x in range(steps):
    print("| |\n---")
  
  print("| |")

def create_ladder():
  step_amount = int(input("How many steps remain?"))
  display_ladder(step_amount)

create_ladder()