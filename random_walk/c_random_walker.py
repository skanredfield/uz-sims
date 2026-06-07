from base_walker import *


class CRandomWalker(BaseWalker):
    """
    Random walker based on the classical paradigms.
    """

    def __init__(self, start_pos, name = None, seed = None, walk_type = WalkType.RAND_AXIS):
        super().__init__(start_pos, name, seed, walk_type)


    def walk(self):
        """
        Performs a step by advancing a unit-length distance in a chosen direction.
        Depending on the value of the walk_type, the axis to walk along can be chosen at random, or all axes can be advanced in a sequence.
        """
        
        match self.walk_type:
            case WalkType.ALL_AXES:
                for i in self.pos:
                    self.pos[i] += self.rand.randint(-1, 1)
            case WalkType.RAND_AXIS | _:
                axis = self.rand.randint(0, self.num_axes-1)
                self.pos[axis] += self.rand.randint(-1, 1)
        self.step_counter[0] += 1
        if self.step_callback is not None:
            self.step_callback()
