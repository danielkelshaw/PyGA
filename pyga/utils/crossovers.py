import abc
import numpy as np


class BaseCrossover(abc.ABC):

    @abc.abstractmethod
    def cross(self, parent_a, parent_b):
        raise NotImplementedError('BaseCrossover::cross()')


class OnePointCrossover(BaseCrossover):

    def cross(self, parent_a, parent_b):
        ix = np.random.randint(1, len(parent_a.position))
        parent_a.position[:ix], parent_a.position[ix:] = \
            parent_b.position[:ix], parent_b.position[ix:]

        return parent_a, parent_b


class TwoPointCrossover(BaseCrossover):

    def cross(self, parent_a, parent_b):
        pass


class UniformCrossover(BaseCrossover):

    def cross(self, parent_a, parent_b):
        pass


class KVectorUniformCrossover(BaseCrossover):

    def cross(self, parent_a, parent_b):
        raise NotImplementedError('KVectorUniformCrossover::cross()')
