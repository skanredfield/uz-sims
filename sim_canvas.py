import matplotlib.pyplot as plt

from body_system import BodySystem
from massive_body import MassiveBody


G = 1


system = BodySystem(G)

body1 = MassiveBody(1000.0, (0, 0, 0), (0, 0, 0))
body2 = MassiveBody(1.0, (10, 0, 0), (0, 10, 0))

system.add_body(body1)
system.add_body(body2)

tspace, rspace, thetaspace = system.evolve_to_time(500)

fig = plt.figure()

ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(tspace, rspace)
ax1.set_title("Cartesian")
ax1.set_xlabel(r"$t$")
ax1.set_ylabel(r"$r$")

ax2 = fig.add_subplot(1, 2, 2, projection='polar')
ax2.plot(thetaspace, rspace)
# ax2.set_ylim(min(rspace)-0.5, max(rspace)+0.5)
ax2.set_title("Polar")
ax2.set_xlabel(r"$\theta$")
ax2.set_ylabel(r"$r$")

plt.tight_layout()

plt.show()