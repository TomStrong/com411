first_number = float(input("Please enter the first number."))
second_number = float(input("Please enter the second number."))

if (first_number > second_number):
  print("The second number is smallest.")
elif (first_number < second_number):
  print("The first number is smallest.")
else:
  print("Both are equal.")