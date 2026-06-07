from base_walker import *


class QRandomWalker:
    """
    Random walker based on the quantum paradigms.
    """

    def __init__(self, start_pos, name = None, seed = None, walk_type = WalkType.RAND_AXIS):
        super().__init__(start_pos, name, seed, walk_type)


    def walk(self):
        pass