import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def animate(frame):
  ax.cla()
  ax.set_xlim(0,720)
  ax.set_ylim(-1,1)
  x = np.arange(0,frame)
  y = np.sin(x * (np.pi/180))
  ax.plot(x,y)

def run():
  sin_anim = animation.FuncAnimation(fig, animate, frames = 720, interval = 100, repeat = False)
  plt.show()

fig, ax = plt.subplots()