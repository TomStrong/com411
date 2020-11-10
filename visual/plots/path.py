import matplotlib.pyplot as plt

def coordinate():
  x_value = input("Enter a x value: ")
  y_value = input("Enter a y value: ")
  return (x_value, y_value)

def path():
  print("Retrieving path...")
  x_values = []
  y_values = []

  for i in range(4):
    data = coordinate()
    x_values.append(data[0])
    y_values.append(data[1])
  
  return [x_values, y_values]

def run():
  values = path()
  plt.plot(values[0], values[1])
  plt.show()