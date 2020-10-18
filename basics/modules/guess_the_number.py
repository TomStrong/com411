import random

def play_guess_the_number():
  minVal = int(input("Please enter the minimum value: "))
  maxVal = int(input("Please enter the maximum value: "))
  number = random.randrange(minVal, maxVal)
  guess = int(input("I am thinking of a number between {} and {}.  Can you guess what it is?".format(minVal, maxVal)))

  while (guess != number):
    if (guess > number):
      print("Your guess is too high.")
    elif (guess < number):
      print("Your guess is too low.")
    
    guess = int(input("Try again: "))

  print("Congratulations! You guessed my number!")

play_guess_the_number()