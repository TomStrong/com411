first_no = int(input("Please enter the first whole number."))
second_no = int(input("Please enter the second whole number."))
third_no = int(input("Please enter the third whole number."))

numbers = [first_no, second_no, third_no]

even_counter = 0
odd_counter = 0

for number in numbers:
  if (number % 2 == 1):
    odd_counter += 1
  else:
    even_counter += 1

print("There were {} even and {} odd numbers.".format(even_counter, odd_counter))