def observed():
  observations = []
  for x in range(5):
    observe = input("Please enter an observation: ")
    observations.append(observe)
  return observations

def remove_observations(observed):
  obs_rem = input("Which observations do you wish to remove? Type 'no' to not remove any.")
  while (obs_rem.lower() != "no"):
    observed.remove(obs_rem)
    obs_rem = input("Which observations do you wish to remove? Type 'no' to not remove any.")
  return observed

def run():
  newList = observed()
  newList = remove_observations(newList)
  newSet = set()
  for item in newList:
    newSet.add((item, newList.count(item))) # adds tuple to set, if tuple exists won't add as it is a set
  print(newSet)

run()