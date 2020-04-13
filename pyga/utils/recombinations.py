import numpy as np
from .crossovers import BaseCrossover


class LineRecombination(BaseCrossover):

    def __init__(self, p=0.25):
        self.p = p

        if not self.p > 0:
            raise ValueError('p must be > 0')

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

    @staticmethod
    def _in_bounds(v, lb, ub):
        return np.logical_and(v >= lb, v <= ub).all()


class IntermediateRecombination(BaseCrossover):

    def cross(self, parent_a, parent_b):
        raise NotImplementedError('IntermediateRecombination::cross()')
