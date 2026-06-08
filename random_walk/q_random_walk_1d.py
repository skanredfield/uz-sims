import numpy as np
import matplotlib.pyplot as plt
from q_random_walker import QRandomWalker


num_steps = 100
num_trials = 100

num_positions = 2 * num_steps + 1

possible_coords = np.linspace(-num_steps, num_steps, num_positions)
dist = { key: 0 for key in possible_coords }

random_walker = None
for _ in range(num_trials):
    random_walker = QRandomWalker([0], num_steps, possible_coords)
    random_walker.walk()
    random_walker.measure()
    dist[random_walker.pos[0]] += 1


fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.bar(possible_coords, random_walker.pos_prob)
ax1.set_title("Probabilities")
ax1.set_xlabel("Position")
ax1.set_ylabel("Probability")
ax2.bar(dist.keys(), dist.values())
ax2.set_title("Histogram")
ax2.set_xlabel("Position")
ax2.set_ylabel("Count")
plt.show()
