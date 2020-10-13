print("Program Started!")
ascii_code = abs(int(input("Please enter an ASCII code: ")))

if (ascii_code in range(32, 127)):
  print("The character represented by the ASCII code {} is {}.".format(ascii_code, chr(ascii_code)))
else:
  print("The code must be between 32 and 126.")

print("Program Ended!")