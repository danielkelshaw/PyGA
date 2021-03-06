import copy
import numpy as np

from .base_ga import BaseGA
from ..individual import Individual
from ..constraints.constraint_manager import ConstraintManager

from ..utils.history import GeneralHistory
from ..utils.mutations import RandomMutation
from ..utils.selections import TournamentSelection, RandomSelection
from ..utils.crossovers import OnePointCrossover
from ..utils.termination_manager import IterationTerminationManager


class SSGA(BaseGA):

    def __init__(self, bounds, n_individuals, n_iterations):
        super().__init__(bounds, n_individuals)

        self.n_iterations = n_iterations
        self.best_individual = None

        self.mutation = RandomMutation()
        self.selection = TournamentSelection()
        self.death_selection = RandomSelection()
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

    def step_optimise(self, fn):

        """
        Progresses the optimisation prcedure by a single iteration.

        Parameters
        ----------
        fn : function
            Fitness function used to evaluate the fitness.
        """

        parent_a = self.selection.select(self.population)
        parent_b = self.selection.select(self.population)

        child_a, child_b = self.crossover.cross(parent_a, parent_b)

        child_a = self.mutation.mutate(child_a)
        child_b = self.mutation.mutate(child_b)

        self.evaluate_fitness(child_a, fn)
        self.update_best(child_a)

        self.evaluate_fitness(child_b, fn)
        self.update_best(child_b)

        idx_pd = np.random.randint(0, len(self.population))
        idx_pe = np.random.randint(0, len(self.population))

        while idx_pd == idx_pe:
            idx_pe = np.random.randint(0, len(self.population))

        for i in sorted([idx_pd, idx_pe], reverse=True):
            self.population.pop(i)

        self.population.extend([child_a, child_b])
        self.history.write_history()

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

        for individual in self.population:
            self.evaluate_fitness(individual, fn)

            if not self.constraint_manager.violates_position(individual):
                self.update_best(individual)

        while not self.termination_manager.termination_check():
            self.step_optimise(fn)
            self.iteration += 1
