import abc
import numpy as np


class BaseHistory(abc.ABC):

    def __init__(self, ga):
        self.ga = ga

    @abc.abstractmethod
    def write_history(self):
        raise NotImplementedError('BaseHistory::write_history()')


class GeneralHistory(BaseHistory):

    def __init__(self, ga):
        super().__init__(ga)

        self.arr_best_fitness = []
        self.arr_mean_fitness = []

    def write_history(self):

        best_fitness = self.ga.best_individual.fitness
        self.arr_best_fitness.append(best_fitness)

        mean_fitness = np.mean([i.fitness for i in self.ga.population])
        self.arr_mean_fitness.append(mean_fitness)
