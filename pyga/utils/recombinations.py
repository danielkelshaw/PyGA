import numpy as np
from .crossovers import BaseCrossover


class BaseRecombination(BaseCrossover):

    """Abstract Base Class for Recombination functionality."""

    def __init__(self, p):

        """
        Initialises Recombination Class.

        Parameters
        ----------
        p : float
            Parameter used in recombination calculations.
        """

        self.p = p

        if not self.p > 0:
            raise ValueError('p must be > 0')

    def cross(self, parent_a, parent_b):
        raise NotImplementedError('BaseRecombination::cross()')

    @staticmethod
    def _in_bounds(v, lb, ub):

        """
        Determines whether vector is within defined bounds.

        Parameters
        ----------
        v : np.ndarray
            Array to determine if within bounds.
        lb : np.ndarray
            Lower bound.
        ub : np.ndarray
            Upper bound.

        Returns
        -------
        bool
            True if v is within the prescribed bounds.
        """

        return np.logical_and(v >= lb, v <= ub).all()


class LineRecombination(BaseRecombination):

    """Implementation of Linear Recombination method."""

    def __init__(self, p=0.25):
        super().__init__(p)

    def cross(self, parent_a, parent_b):
        lb, ub = parent_a.lb, parent_b.ub

        a = np.random.uniform(-self.p, 1 + self.p)
        b = np.random.uniform(-self.p, 1 + self.p)

        for i in range(len(parent_a.position)):
            t = a * parent_a.position[i] + (1 - a) * parent_b.position[i]
            s = b * parent_b.position[i] + (1 - b) * parent_a.position[i]

            if self._in_bounds(t, lb, ub) and self._in_bounds(s, lb, ub):
                parent_a.position[i] = t
                parent_b.position[i] = s

        return parent_a, parent_b


class IntermediateRecombination(BaseRecombination):

    """Implementation of Intermediate Recombination method."""

    def __init__(self, p=0.25):
        super().__init__(p)

    def cross(self, parent_a, parent_b):
        lb, ub = parent_a.lb, parent_b.ub

        for i in range(len(parent_a.position)):
            a = np.random.uniform(-self.p, 1 + self.p)
            b = np.random.uniform(-self.p, 1 + self.p)

            t = a * parent_a.position[i] + (1 - a) * parent_b.position[i]
            s = b * parent_b.position[i] + (1 - b) * parent_a.position[i]

            if self._in_bounds(t, lb, ub) and self._in_bounds(s, lb, ub):
                parent_a.position[i] = t
                parent_b.position[i] = s

        return parent_a, parent_b
