import matplotlib.pyplot as plt
import matplotlib.animation as animation

def init():
  squares = {
    "small":([3,3,4,4,3],[3,4,4,3,3]),
    "medium":([2,2,5,5,2],[2,5,5,2,2]),
    "large":([1,1,6,6,1],[1,6,6,1,1])
  }
  return squares

def animate(frame):
  squares = init()
  ax.cla()
  ax.set_xlim(0,7)
  ax.set_ylim(0,7)
  ax.plot(squares[frame][0],squares[frame][1])

def run():
  sqaure_anim = animation.FuncAnimation(fig, animate, frames = ["small","medium","large"], interval = 1000)
  plt.show()

fig, ax = plt.subplots()