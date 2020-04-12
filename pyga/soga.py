import copy
import numpy as np
from .individual import Individual


class SOGA:

    def __init__(self, lb, ub, n_individuals, n_iterations):

        """
        Single-Objective Genetic Algorithm.

        Parameters
        ----------
        lb : list or np.ndarray
            Lower bound of the search space.
        ub : list of np.ndarray
            Upper bound of the search space.
        n_individuals : int
            Number of individuals in the population.
        n_iterations : int
            Number of iterations for the optimisation.

        Attributes
        ----------
        iteration : int
            Current iteration of the optimisation process.
        population : list of Individual
            Current state of the population for the optimisation.
        best_inidividual : Individual
            The individual with the most-optimum fitness.
        """

        if len(lb) != len(ub):
            raise ValueError(f'len(lb): {len(lb)} != len(ub): {len(ub)}')

        self.lb = np.asarray(lb)
        self.ub = np.asarray(ub)

        self.n_indviduals = n_individuals
        self.n_iterations = n_iterations

        self.iteration = 0

        self.population = []
        self.best_individual = None

    def reset_environment(self):

        """Responsible for resetting the optimisation environment."""

        self.iteration = 0
        self.population = []
        self.best_individual = None

    def initialise_population(self):

        """Generates the population list of Individuals."""

        for _ in range(self.n_indviduals):
            self.population.append(Individual(self.lb, self.ub))

    def termination_check(self):

        """Checks if the optimisation process is complete."""

        if self.iteration > self.n_iterations:
            return True
        else:
            return False

    def update_best(self, individual):

        """
        Updates the best_individual according to the fitness of the
        individual which is passed as an argument.

        Parameters
        ----------
        individual : Individual
            Object to compare fitness with best_individual.
        """

        if individual.fitness < self.best_individual.fitness:
            self.best_individual = copy.deepcopy(individual)

    # TODO >> These methods can be part of a `utils` file.
    @staticmethod
    def select(population):
        pass

    @staticmethod
    def crossover(parent_a, parent_b):
        pass

    @staticmethod
    def mutate(self):
        pass

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

        while not self.termination_check():

            for individual in self.population:
                self.evaluate_fitness(individual, fn)

            _population = []
            for i in range(self.n_indviduals // 2):
                parent_a, parent_b = self.select(self.population)
                child_a, child_b = self.crossover(parent_a, parent_b)
                child_a, child_b = self.mutate(child_a), self.mutate(child_b)
                _population.extend([child_a, child_b])

            self.iteration += 1
