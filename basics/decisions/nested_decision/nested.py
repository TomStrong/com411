cover_type = str(input("What type of cover does the book have?"))

if (cover_type.lower() == "soft"):
  perfect_bound = str(input("Is the book perfect-bound?"))

  if (perfect_bound == "yes"):
    print("Soft cover, perfect bound books are very popular!")
  elif (perfect_bound == "no"):
    print("Soft covers with coils or stitches are great for short books.")
  else:
    print("That was not an option.")

elif (cover_type.lower() == "hard"):
  print("Books with hard covers can be more expensive!")

else:
  print("That's not an option.")