import abc
import copy
import itertools as it
import numpy as np


class BaseSelection(abc.ABC):

    @abc.abstractmethod
    def preprocess(self, population):
        raise NotImplementedError('BaseSelection::preprocess()')

    @abc.abstractmethod
    def select(self, population):
        raise NotImplementedError('BaseSelection::select()')


class RandomSelection(BaseSelection):

    def preprocess(self, population):
        pass

    def select(self, population):
        return copy.deepcopy(np.random.choice(population))


class TournamentSelection(BaseSelection):

    def __init__(self, t_size=2):

        if t_size < 2:
            raise ValueError('t_size must be >= 1')

        self.t_size = t_size

    def preprocess(self, population):
        pass

    def select(self, population):
        best = copy.deepcopy(np.random.choice(population))
        for i in range(1, self.t_size):
            nxt = copy.deepcopy(np.random.choice(population))
            if nxt.fitness < best.fitness:
                best = nxt
        return best


class FitnessProportionateSelection(BaseSelection):

    def __init__(self):
        self.cdf = None

    def preprocess(self, population):
        flist = [1 / i.fitness for i in population]
        self.cdf = list(it.accumulate(flist, lambda x, y: x + y))

    def select(self, population):
        n = np.random.uniform(0, self.cdf[-1])
        for i in range(1, len(self.cdf)):
            if self.cdf[i - 1] < n <= self.cdf[i]:
                return copy.deepcopy(population[i])

        return copy.deepcopy(population[0])


class TruncationSelection(BaseSelection):

    def preprocess(self, population):
        pass

    def select(self, population):
        pass


class StochasticUniversalSamplingSelection(BaseSelection):

    def __init__(self):
        self.population = None
        self.flist = None
        self.cdf = None
        self.index = None
        self.value = None

    def preprocess(self, population):
        self.population = self._shuffle(copy.deepcopy(population))
        self.flist = [1 / i.fitness for i in self.population]
        self.cdf = list(it.accumulate(self.flist, lambda x, y: x + y))
        self.index = 0
        self.value = np.random.uniform(0, self.cdf[-1] / len(self.population))

    def select(self, population):
        while self.index < self.value:
            self.index += 1
        self.value += self.cdf[-1] / len(self.population)

        if self.index > len(self.population) - 1:
            return self.population[-1]

        return self.population[self.index]

    @staticmethod
    def _shuffle(population):
        for i in range(len(population) - 1, 1, -1):
            j = np.random.randint(0, i + 1)
            population[i], population[j] = population[j], population[i]

        return population
