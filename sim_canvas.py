import matplotlib.pyplot as plt
import numpy as np

from massive_body import MassiveBody


G = 1

body1 = MassiveBody(1000.0, (0, 0, 0), (0, 0, 0))
body2 = MassiveBody(1.0, (10, 0, 0), (0, 10, 0))

mu = -G * body1.mass * body2.mass

tspace = np.linspace(0, 500, 500)
rspace = []
thetaspace = []

for t in tspace:
    dx = body2.x - body1.x
    dy = body2.y - body1.y
    dr = np.sqrt(dx**2 + dy**2)
    rspace.append(dr)
    force = mu / dr**2

    theta = np.atan2(dy, dx)
    thetaspace.append(theta)
    fx = np.cos(theta) * force
    fy = np.sin(theta) * force
    fvec = (fx, fy, 0)

    dt = t / 1000.0

    # update the orbiter's parameters
    body2.update(dt, fvec)


fig = plt.figure()

ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(tspace, rspace)
ax1.set_title("Cartesian")
ax1.set_xlabel(r"$t$")
ax1.set_ylabel(r"$r$")

ax2 = fig.add_subplot(1, 2, 2, projection='polar')
ax2.plot(thetaspace, rspace)
ax2.set_title("Polar")
ax2.set_xlabel(r"$\theta$")
ax2.set_ylabel(r"$r$")

plt.tight_layout()

plt.show()