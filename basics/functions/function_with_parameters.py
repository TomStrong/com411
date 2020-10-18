def climb_ladder(steps_left, steps_crossed):
  if (steps_left > steps_crossed):
    print("Still some way to go!")
  elif (steps_left < steps_crossed):
    print("We are almost there!")

climb_ladder(5,2)
climb_ladder(2,5)