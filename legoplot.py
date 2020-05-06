import math
import numpy as np
import matplotlib.pyplot as plt

WIDTH = 1
HEIGHT = 3
ANGLE = (1, 10)

inter_width = 2 * WIDTH
inter_height = 2 * HEIGHT
max_radius = int(math.ceil(
    math.sqrt(inter_width**2 + inter_height**2)))
angle = 2 * math.asin(math.sqrt(float(ANGLE[0]) / ANGLE[1]))

x = []
y = []
for w in xrange(inter_width + 1):
    for h in xrange(inter_height + 1):
        x.append(math.cos(angle) * w - math.sin(angle) * h)
        y.append(math.sin(angle) * w + math.cos(angle) * h)


fig, ax = plt.subplots()
ax.plot(x, y, 'x')
ax.xaxis.set_ticks(np.arange(-max_radius - 1,  max_radius + 1, 1))
ax.yaxis.set_ticks(np.arange(-1, max_radius + 1, 1))
ax.set_aspect('equal')
ax.grid()
plt.show()
