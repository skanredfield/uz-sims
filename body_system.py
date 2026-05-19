import numpy as np


class BodySystem:

    def __init__(self, grav_const):
        self.bodies = []
        self.grav_const = grav_const

    def add_body(self, body):
        self.bodies.append(body)
        
    def remove_body(self, body):
        self.bodies.remove(body)

    def evolve_to_time(self, frames):
        tspace = np.linspace(0, frames, frames)
        rspace = np.empty(frames)
        thetaspace = np.empty(frames)

        for i, t in enumerate(tspace):
            for j, body1 in enumerate(self.bodies):
                for k, body2 in enumerate(self.bodies):
                    if j == k:
                        continue

                    mu = -self.grav_const * body1.mass * body2.mass

                    dx = body2.x - body1.x
                    dy = body2.y - body1.y
                    dr = np.sqrt(dx**2 + dy**2)
                    rspace[i] = dr
                    force = mu / dr**2

                    theta = np.atan2(dy, dx)
                    thetaspace[i] = theta
                    fx = np.cos(theta) * force
                    fy = np.sin(theta) * force
                    fvec = (fx, fy, 0)
                    neg_fvec = (-fx, -fy, 0)

                    dt = t / 1000.0

                    # update the orbiter's parameters
                    body2.update(dt, fvec)
                    body1.update(dt, neg_fvec)

        return (tspace, rspace, thetaspace)