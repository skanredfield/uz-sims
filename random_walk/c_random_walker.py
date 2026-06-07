import random
from enum import Enum
from numpy import sqrt, sum


class WalkType(Enum):
    """
    Specifies the walking behaviour.
    """
    RAND_AXIS = 1
    ALL_AXES = 2

class CRandomWalker:
    """
    Random walker based on the classical paradigms.
    """

    def __init__(self, start_pos, name = None, seed = None, walk_type = WalkType.RAND_AXIS):
        """
        Initializes a random walker.

        Args:
            start_pos (list): Starting position of the walker as a list of coordinates.
            name (string, optional): The name of the walker (can be used for printing).
            seed (int, optional): The seed for the random generator.
            walk_type (WalkType, optional): An enumerable representing walking behaviour (default is WalkType.RAND_AXIS).

        Returns:
            CRandomWalker: A CRandomWalker instance.
        """

        self.rand = random.Random(seed)
        self.name = name
        self.step_callback = None
        self.walk_type = walk_type

        # declare a counter as a mutable type
        self.step_counter = [0]

        # initialize the position dictionary for any number of dimensions, 
        # depending on the size of the start_pos tuple/list
        self.num_axes = len(start_pos)
        self.pos = {}
        for i, coord in enumerate(start_pos):
            self.pos[i] = coord

    @property
    def get_pos_data(self) -> str:
        """ Nicely formatted position as a string. """
        r = sqrt(sum([x**2 for x in self.pos.values()]))
        axis_labels = "".join([f"x{i}, " for i in range(len(self.pos))])
        coords = "".join([f"{val}, " for val in self.pos.values()])
        return f"{self.name}: (t, {axis_labels}r) = ({self.step_counter[0]}, {coords}{round(r, 3)})"


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
                axis = random.randint(0, self.num_axes-1)
                self.pos[axis] += self.rand.randint(-1, 1)
        self.step_counter[0] += 1
        if self.step_callback is not None:
            self.step_callback()
