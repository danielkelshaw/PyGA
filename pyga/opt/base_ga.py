import abc


class BaseGA(abc.ABC):

    def __init__(self, bounds, n_individuals):

        if not isinstance(bounds, dict):
            raise TypeError('bounds must be dict.')

        if not n_individuals % 2 == 0:
            raise ValueError('Please ensure n_individuals is even.')

        self.bounds = bounds
        self.pnames = list(bounds.keys())

        self.n_individuals = n_individuals
        self.population = []

        self.iteration = 0

    @abc.abstractmethod
    def reset_environment(self):
        raise NotImplementedError('BaseGA::reset_environment()')

    @abc.abstractmethod
    def initialise_population(self):
        raise NotImplementedError('BaseGA::initialise_population()')

    @staticmethod
    @abc.abstractmethod
    def evaluate_fitness(individual, fn):
        raise NotImplementedError('BaseGA::evaluate_fitness()')

    @abc.abstractmethod
    def step_optimise(self, fn):
        raise NotImplementedError('BaseGA::step_optimise()')

    @abc.abstractmethod
    def optimise(self, fn):
        raise NotImplementedError('BaseGA::optimise()')
