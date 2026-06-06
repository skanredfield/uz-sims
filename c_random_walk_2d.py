import numpy as np
import matplotlib.pyplot as plt
from c_random_walker import CRandomWalker


num_steps = 20
num_trials = 100

dist = {}
nums = np.linspace(-num_steps, num_steps, (2 * num_steps + 1))  
for i in nums:
    for j in nums:
        dist[(i, j)] = 0


for _ in range(num_trials):
    random_walker = CRandomWalker([0, 0])
    for i in range(num_steps):
        random_walker.walk()
        dist[(random_walker.pos[0], random_walker.pos[1])] += 1

axis_keys = list(zip(*dist.keys()))
z_anchor = np.zeros_like(dist.values())
dx = dy = 0.9 * np.ones_like(dist.values())
dz = dist.values()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.bar3d(axis_keys[0], axis_keys[1], z_anchor, dx, dy, dz)
plt.show()