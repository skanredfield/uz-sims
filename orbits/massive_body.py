class MassiveBody:

    def __init__(self, id, mass, position: tuple, velocity: tuple):

        self.id = id
        
        self.mass = mass
        self.position = position
        x, y, z = position
        self.x = x
        self.y = y
        self.z = z
        
        self.velocity = velocity
        vx, vy, vz = velocity
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def update(self, timestep, force):
        fx, fy, fz = force 
        ax = fx / self.mass
        ay = fy / self.mass
        self.vx += ax * timestep
        self.vy += ay * timestep
        self.x += self.vx * timestep
        self.y += self.vy * timestep