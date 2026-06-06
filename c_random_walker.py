import random
import functools


class CRandomWalker:

    def __init__(self, start_pos, name = None, seed = None):
        self.rand = random.Random(seed)
        self.name = name
        self.step_callback = None

        # initialize the position dictionary for any number of dimensions, 
        # depending on the size of the start_pos tuple/list
        self.pos = {}
        for coord, i in enumerate(start_pos):
            self.pos[i] = coord

    def set_callback(self, step_callback, *args):
        self.step_callback = functools.partial(step_callback, *args)

    def walk(self):
        for i in self.pos:
            self.pos[i] += self.rand.randint(-1, 1)
        if self.step_callback is not None:
            self.step_callback()
