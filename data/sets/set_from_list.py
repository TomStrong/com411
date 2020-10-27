def observed():
  observations = []
  for x in range(7):
    observe = input("Observation {}".format(x+1))
    observations.append(observe)
  return observations

def run():
  print("Counting observations...")
  newList = observed()
  newSet = set()
  for item in newList:
    newSet.add((item, newList.count(item))) # adds tuple to set, if tuple exists won't add as it is a set
  print(newSet)

run()