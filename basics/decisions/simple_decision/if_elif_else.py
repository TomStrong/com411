direction = str(input("Towards which direction should I paint (up, down, left or right)?"))

if (direction.lower() == "up"):
  print("I am painting in the upward direction!")
elif (direction.lower() == "down"):
  print("I am painting in the downward direction!")
elif (direction.lower() == "left"):
  print("I am painting to the left.")
elif (direction.lower() == "right"):
  print("I am painting to the right.")
else:
  print("That is not a valid direction.")