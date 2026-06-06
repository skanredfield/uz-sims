import numpy as np
import matplotlib.pyplot as plt
from c_random_walker import CRandomWalker


num_steps = 100
num_trials = 100

dist = np.linspace(-num_steps, num_steps, (2 * num_steps + 1))  
dist = { key: 0 for key in dist }

for _ in range(num_trials):
    random_walker = CRandomWalker([0])
    # random_walker.set_callback(print, random_walker.pos)
    for i in range(num_steps):
        random_walker.walk()
        dist[random_walker.pos[0]] += 1


plt.bar(dist.keys(), dist.values())
plt.show()