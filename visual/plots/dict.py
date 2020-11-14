import matplotlib.pyplot as plt
import random as rand

def data():
  paths = {}
  paths["style"] = input("What type of line would you like? \nDotted (:) Dashed (--) Solid (-)").lower()
  paths["colour"] = input("What colour line would you like? \nRed (R) Green (G) Blue (B)").lower()
  paths["marker"] = input("What type of marker do you want? \nCircle (O) Square (S) Triangle (^)").lower()
  return paths

def coordinates():
  x_coords = []
  y_coords = []
  for x in range(rand.randint(0,100)):
    x_coords.append(rand.randint(0,100))
    y_coords.append(rand.randint(0,100))

  return [x_coords, y_coords]

def generate():
  amount = int(input("How many lines would you like to display?"))
  
  for i in range(amount):
    values = data()
    coords = coordinates()
    plt.plot(coords[0], coords[1], values["colour"] + values["marker"] + values["style"])

  plt.show()

def run():
  print("Running....")
  generate()