room = str(input("Where should I look?"))

if (room.lower() == "in the bedroom"):
  sub_location = str(input("Where in the bedroom should I look?"))
  if (sub_location.lower() == "under the bed"):
    print("Found some shoes but no battery.")
  else:
    print("Found some mess but no battery.")
elif (room.lower() == "in the bathroom"):
  sub_location = str(input("Where in the bathroom should I look?"))
  if (sub_location.lower() == "in the bathtub"):
    print("Found a rubber duck but no battery.")
  else:
    print("Found a wet surface but no battery.")
elif (room.lower() == "in the lab"):
  sub_location = str(input("Where in the lab should I look?"))
  if (sub_location.lower() == "on the table"):
    print("Yes! I found my battery!")
  else:
    print("Found some tools but no battery.")
else:
  print("I do not know where that is but I will keep looking.")