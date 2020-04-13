import abc
import numpy as np


class BaseCrossover(abc.ABC):

    @abc.abstractmethod
    def cross(self, parent_a, parent_b):
        raise NotImplementedError('BaseCrossover::cross()')


class OnePointCrossover(BaseCrossover):

    def cross(self, parent_a, parent_b):
        c = np.random.randint(0, len(parent_a.position) + 1)

        if c != 0:
            for i in range(c, len(parent_a.position)):
                parent_a.position[i], parent_b.position[i] = \
                    parent_b.position[i], parent_a.position[i].copy()

        return parent_a, parent_b


class TwoPointCrossover(BaseCrossover):

    def cross(self, parent_a, parent_b):
        c = np.random.randint(1, len(parent_a.position) + 1)
        d = np.random.randint(1, len(parent_a.position) + 1)

        if c > d:
            c, d = d, c

        if c != d:
            for i in range(c, d):
                parent_a.position[i], parent_b.position[i] = \
                    parent_b.position[i], parent_a.position[i].copy()

        return parent_a, parent_b


class UniformCrossover(BaseCrossover):

    def __init__(self, p_swap):
        self.p_swap = p_swap or None

        if self.p_swap is not None and not self.p_swap <= 0.5:
            raise ValueError('p_swap must be <= 0.5')

    def cross(self, parent_a, parent_b):

        if self.p_swap is None:
            self.p_swap = 1 / len(parent_a.position)
        if len(parent_a.position) == 1:
            self.p_swap = 0.5

        for i in range(1, len(parent_a.position)):
            if self.p_swap >= np.random.uniform():
                parent_a.position[i], parent_b.position[i] = \
                    parent_b.position[i], parent_a.position[i].copy()

        return parent_a, parent_b


class KVectorUniformCrossover(BaseCrossover):

    def cross(self, parent_a, parent_b):
        raise NotImplementedError('KVectorUniformCrossover::cross()')
