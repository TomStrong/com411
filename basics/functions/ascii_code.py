print("Program Started!")
ascii_char = str(input("Please enter a standard character: "))

if (len(ascii_char) == 1):
  print("The ASCII code for {} is {}.".format(ascii_char, ord(ascii_char)))
else:
  print("A character was not entered.")

print("Program Ended!")