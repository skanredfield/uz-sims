from random_walker import RandomWalker

seed = 245
random_walker = RandomWalker(seed, [0])
random_walker.set_callback(print, random_walker.pos)

num_steps = 20

for i in range(num_steps):
    random_walker.walk()