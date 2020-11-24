import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def animate(frame):
  line.set_ydata(np.sin(x + frame / 50))
  return line,
  

def run():
  sin_anim = animation.FuncAnimation(fig, animate, interval = 20, blit = True)
  plt.show()

fig, ax = plt.subplots()

ax.set_xlim(0,2*np.pi)
ax.set_ylim(-1,1)
x = np.arange(0,2*np.pi,0.01)
y = np.sin(x)
line, = ax.plot(x,y)