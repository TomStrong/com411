import matplotlib.pyplot as plt

def read_data(file_path):
  with open(file_path, "r") as file:
    lines = file.readlines()
  
  xAxis = None
  yAxis = None
  xVals = []
  yVals = []
  
  for line in lines:
    values = line.split()

    if (xAxis == None):
      xAxis = values[0]
      yAxis = values[1]
    else:
      xVals.append(int(values[0]))
      yVals.append(int(values[1]))

  axis = [xAxis, yAxis]
  vals = [xVals, yVals]

  return (axis, vals)

def run():
  data = read_data("visual/subplots/temps.txt")
  fig, axs = plt.subplots(2, 2)
  axs[0,0].plot(data[1][0], data[1][1])
  axs[0,0].set_xlabel(data[0][0])
  axs[0,0].set_ylabel(data[0][1])
  plt.show()

run()