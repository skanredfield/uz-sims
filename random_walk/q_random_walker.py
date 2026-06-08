import numpy as np
from base_walker import *
from typing import override


class QRandomWalker(BaseWalker):
    """
    Random walker based on the quantum paradigms.
    Adapted from https://susan-stepney.blogspot.com/2014/02/mathjax.html by Susan Stepney.
    """

    def __init__(self, start_pos, num_steps, possible_coords, name = None, seed = None, walk_type = WalkType.RAND_AXIS):
        """
        Initializes a quantum random walker.

        Args:
            start_pos (list): Starting position of the walker as a list of coordinates.
            num_steps (int): Number of steps to take.
            possible_coords (list): The range of all possible integer positions on the axis.
            name (string, optional): The name of the walker (can be used for printing).
            seed (int, optional): The seed for the random generator.
            walk_type (WalkType, optional): An enumerable representing walking behaviour (default is WalkType.RAND_AXIS).

        Returns:
            CRandomWalker: A CRandomWalker instance.
        """
        super().__init__(start_pos, name, seed, walk_type)

        self.num_steps = num_steps
        self.num_positions = len(possible_coords)
        self.possible_coords = possible_coords

        # Define the two orthogonal states.
        c0 = np.array([1, 0])  # |0>
        c1 = np.array([0, 1])  # |1>
        # Compute projections.
        c00 = np.outer(c0, c0)  # |0><0| 
        c01 = np.outer(c0, c1)  # |0><1| 
        c10 = np.outer(c1, c0)  # |1><0| 
        c11 = np.outer(c1, c1)  # |1><1|

        # Define the operator that performs the choice of direction
        choice_op = (c00 + c01 + c10 - c11) / np.sqrt(2.0)
        # Define the operators that increment or decrement the possible position state
        increment_op = np.roll(np.eye(self.num_positions), 1, axis=0)
        decrement_op = np.roll(np.eye(self.num_positions), -1, axis=0)
        # Introduce the step operator
        step_op = np.kron(increment_op, c00) + np.kron(decrement_op, c11)
        # The walk operator combines the choice and step operators into one
        self.walk_op = step_op.dot(np.kron(np.eye(self.num_positions), choice_op))

        # Mark the current position as identity in a list of possible positions
        pos0 = np.zeros(self.num_positions)
        pos0[self.pos[0] + num_steps - 1] = 1
        # Define the initial wave function
        psi0 = np.kron(pos0, (c0 + c1 * 1j) / sqrt(2.0))
        self.psiN = psi0
        self.pos_prob = np.empty(self.num_positions)


    @override
    def walk(self):
        """
        Determines the possible position space by applying the walk operator on the wave function.
        """
        self.psiN = np.linalg.matrix_power(self.walk_op, self.num_steps).dot(self.psiN)


    def measure(self):
        """
        Performs a measurement to collapse the wavefunction and settle on a probable position. This function actually 'walks' the quantum walker.
        """
        for k in range(self.num_positions):
            posn = np.zeros(self.num_positions)
            posn[k] = 1     
            M_hat_k = np.kron(np.outer(posn, posn), np.eye(2))
            proj = M_hat_k.dot(self.psiN)
            self.pos_prob[k] = proj.dot(proj.conjugate()).real
        self.pos[0] = np.random.choice(self.possible_coords, size=1, p=self.pos_prob)[0]