name = str(input("What is your human name?"))
age = int(input("How old are you (in years)?"))
height = float(input("How tall are you (in meters)?"))
weight = float(input("How much do you weigh (in kilograms)?"))

print("{} you are {} years old and your bmi is {:.2f}".format(name, age, weight/(height**2)))