import matplotlib.pyplot as plt

from body_system import BodySystem
from massive_body import MassiveBody


G = 1


system = BodySystem(G)

body1 = MassiveBody(1, 1000.0, (0, 0, 0), (0, 0, 0))
body2 = MassiveBody(2, 1.0, (10, 0, 0), (0, 10, 0))
body3 = MassiveBody(3, 2.0, (7, 2, 0), (5, 5, 0))

system.add_body(body1)
system.add_body(body2)
# system.add_body(body3)

id = body2.id
tspace, rspace, thetaspace, odist = system.evolve_to_time(10)
print(rspace)

fig = plt.figure()

ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(tspace, odist[id])
ax1.set_title("Cartesian")
ax1.set_xlabel(r"$t$")
ax1.set_ylabel(r"$r$")

ax2 = fig.add_subplot(1, 2, 2, projection='polar')
ax2.plot(thetaspace[id], rspace[id])
# ax2.set_ylim(min(rspace)-0.5, max(rspace)+0.5)
ax2.set_title("Polar")
ax2.set_xlabel(r"$\theta$")
ax2.set_ylabel(r"$r$")

plt.tight_layout()

plt.show()