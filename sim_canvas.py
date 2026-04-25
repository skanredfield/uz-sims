import matplotlib.pyplot as plt
import numpy as np

G = 1
m1 = 1000.0
m2 = 1.0
mu = -G * m1 * m2

m1_x = 0
m1_y = 0
m2_x = 10
m2_y = 0
m2_vx = 0
m2_vy = 10

tspace = np.linspace(0, 1000, 1000)
rspace = []

for t in tspace:
    dx = m2_x - m1_x
    dy = m2_y - m1_y
    dr = np.sqrt(dx**2 + dy**2)
    rspace.append(dr)
    force = mu / dr**2

    theta = np.atan2(dy, dx)
    fx = np.cos(theta) * force
    fy = np.sin(theta) * force
    ax = fx / m2
    ay = fy / m2

    dt = t / 1000.0

    m2_vx += ax * dt
    m2_vy += ay * dt
    m2_x += m2_vx * dt
    m2_y += m2_vy * dt

plt.plot(tspace, rspace)
plt.xlabel(r"$t$")
plt.ylabel(r"$r$")
plt.show()