import numpy as np
import matplotlib.pyplot as plt
from c_random_walker import CRandomWalker


num_steps = 30
num_trials = 40

dist = {}
steps = np.linspace(-num_steps, num_steps, (2 * num_steps + 1))  
for i in steps:
    for j in steps:
        for k in steps:
            dist[(i, j, k)] = 0


for _ in range(num_trials):
    random_walker = CRandomWalker([0, 0, 0])
    for i in range(num_steps):
        random_walker.walk()
        dist[(random_walker.pos[0], random_walker.pos[1], random_walker.pos[2])] += 1

axis_keys = list(zip(*dist.keys()))
z_anchor = np.zeros_like(dist.values())
dx = dy = 0.9 * np.ones_like(dist.values())
dz = np.empty(len(dist)) 
zmin = float('inf')
zmax = -float('inf')
# iterate to find the min and max in a single pass (and also make the iterable into a numpy array)
for i, val in enumerate(dist.values()):
    dz[i] = val
    if val > zmax:
        zmax = val
    if val < zmin:
        zmin = val

# create a color mapping to represent the 3rd dimension of data
cmap = plt.get_cmap('jet')
rgba = [cmap((z - zmin) / zmax) for z in dz]

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.bar3d(axis_keys[0], axis_keys[1], z_anchor, dx, dy, dz, color=rgba)
plt.show()