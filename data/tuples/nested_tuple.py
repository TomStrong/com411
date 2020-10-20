def steps():
  likelihoods = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
  return likelihoods

def run():
  stepsChance = steps()
  good_steps = []
  bad_steps = []
  for chance in stepsChance:
    if (chance[1] >= 50):
      bad_steps.append(chance)
    else:
      good_steps.append(chance)

  print("Good steps: {}, Bad steps: {}".format(len(good_steps), len(bad_steps)))

run()