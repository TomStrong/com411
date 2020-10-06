adventure = str(input("What type of adventure should I have?"))

if (adventure.lower() == "short" or adventure.lower() == "scary"):
  print("Entering the dark forest!")
elif (adventure.lower() == "safe" or adventure.lower() == "long"):
  print("Taking the safe route!")
else:
  print("Not sure which route to take.")