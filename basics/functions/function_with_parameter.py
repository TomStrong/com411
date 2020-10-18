def escape_by(plan):
  if (plan.lower() == "jumping over"):
    print("We cannot escape that way! The boulder is too big!")
  elif (plan.lower() == "running around"):
    print("We cannot escape that way! The boulder is moving too fast!")
  elif (plan.lower() == "going deeper"):
    print("That might just work! Let's go deeper!")
  else:
    print("We cannot escape that way! The boulder is in the way!")

escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")
escape_by("waiting")