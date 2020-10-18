def identify():
  response = str(input("What lies before us?"))
  if (response.lower() == "a large boulder"):
    print("It's time to run!")
  else:
    print("We will be fine.")

identify()