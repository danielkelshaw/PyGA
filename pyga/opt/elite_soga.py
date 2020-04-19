import copy

from .base_ga import BaseGA
from ..individual import Individual
from ..constraints.constraint_manager import ConstraintManager

from ..utils.history import GeneralHistory
from ..utils.mutations import RandomMutation
from ..utils.selections import TournamentSelection
from ..utils.crossovers import OnePointCrossover
from ..utils.termination_manager import IterationTerminationManager


class EliteSOGA(BaseGA):

    def __init__(self, bounds, n_individuals, n_iterations):
        super().__init__(bounds, n_individuals)

        self.n_iterations = n_iterations
        self.best_individual = None

        self.mutation = RandomMutation()
        self.selection = TournamentSelection()
        self.crossover = OnePointCrossover()

        self.history = GeneralHistory(self)
        self.termination_manager = IterationTerminationManager(self)
        self.constraint_manager = ConstraintManager(self)

    def reset_environment(self):

        """Responsible for resetting the optimisation environment."""

        self.iteration = 0
        self.population = []
        self.best_individual = None

    def initialise_population(self):

        """Generates the population list of Individuals."""

        for _ in range(self.n_individuals):
            self.population.append(Individual(self.bounds))

    def update_best(self, individual):

        """
        Updates the best_individual according to the fitness of the
        individual which is passed as an argument.

        Parameters
        ----------
        individual : Individual
            Object to compare fitness with best_individual.
        """

        if self.best_individual is None:
            self.best_individual = copy.deepcopy(individual)
        elif individual.fitness < self.best_individual.fitness:
            self.best_individual = copy.deepcopy(individual)

    @staticmethod
    def evaluate_fitness(individual, fn):

        """
        Sets the fitness of the individual passed in.

        Parameters
        ----------
        individual : Individual
            Individual for which to assess the fitness.
        fn : function
            Fitness function used to evaluate the fitness.
        """

        individual.fitness = fn(individual.position)

    # TODO >> Implement EliteSOGA::step_optimise()
    def step_optimise(self, fn):
        raise NotImplementedError('EliteSOGA::step_optimise()')

    def optimise(self, fn):

        """
        Responsible for managing the optimisation process.

        Parameters
        ----------
        fn : function
            Fitness function used to evaluate the fitness.
        """

        self.reset_environment()
        self.initialise_population()

        while not self.termination_manager.termination_check():
            self.step_optimise(fn)
            self.iteration += 1
