import abc
import copy
import numpy as np
import itertools as it


class BaseSelection(abc.ABC):

    """Abstract Base Class for all Selection functionality."""

    @abc.abstractmethod
    def preprocess(self, population):

        """
        Responsible for any preprocessing required for the selection
        method - this can be useful for reducing computational costs
        in some instances.

        Parameters
        ----------
        population : list
            List of individuals.
        """

        raise NotImplementedError('BaseSelection::preprocess()')

    @abc.abstractmethod
    def select(self, population):

        """
        Selects an individual from the population.

        Parameters
        ----------
        population : list
            List from which to select an individual.

        Returns
        -------
        Individual
            Copy of the individual selected from the population.
        """

        raise NotImplementedError('BaseSelection::select()')


class RandomSelection(BaseSelection):

    """Implementation of 'random selection'."""

    def preprocess(self, population):
        pass

    def select(self, population):
        return copy.deepcopy(np.random.choice(population))


class TournamentSelection(BaseSelection):

    """Implementation of 'tournament selection'."""

    def __init__(self, t_size=2):

        """
        Initialises the TournamentSelection Class.

        Parameters
        ----------
        t_size : int
            Tournament size.
        """

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

    """Implementation of 'fitness-proportionate selection'."""

    def __init__(self):

        """
        Initialises the FitnessProportionateSelection Class.

        Attributes
        ----------
        cdf : list
            Cumulative fitness for the population.
        """

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

    """Implementation of 'truncation selection'."""

    def preprocess(self, population):
        pass

    def select(self, population):
        pass


class StochasticUniversalSamplingSelection(BaseSelection):

    """Implementation of 'stochastic universal sampling selection'."""

    def __init__(self):

        """
        Initialises StochasticUniversalSamplingSelection Class.

        Attributes
        ----------
        population : list
            Holds the current population.
        flist : list
            Fitnesses of all members of the population.
        cdf : list
            Cumulative fitness for the population.
        index : int
            Current index from which to select a population member.
        value : float
            Value used to determine the index from which to sample.
        """

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

        """
        Randomly shuffles the members of the provided population.

        Parameters
        ----------
        population : list
            The population list for which to randomly shuffle.

        Returns
        -------
        population : list
            Shuffled population.
        """

        for i in range(len(population) - 1, 1, -1):
            j = np.random.randint(0, i + 1)
            population[i], population[j] = population[j], population[i]

        return population
