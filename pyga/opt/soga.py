import copy

from .base_ga import BaseGA
from ..individual import Individual
from ..constraints.constraint_manager import ConstraintManager

from ..utils.history import GeneralHistory
from ..utils.mutations import RandomMutation
from ..utils.selections import TournamentSelection
from ..utils.crossovers import OnePointCrossover
from ..utils.termination_manager import IterationTerminationManager


class SOGA(BaseGA):

    def __init__(self, bounds, n_individuals, n_iterations):

        """
        Initialiser for SOGA class.

        Parameters
        ----------
        bounds : dict
            Lower and upper bounds of the search space.
        n_individuals : int
            Number of individuals for use in the population.
        n_iterations : int
            Number of iterations to optimise for.

        Attributes
        ----------
        best_individual : Individual
            The current best individual from the optimisation.
        mutation : BaseMutation
            Muation method to use.
        selection : BaseSelection
            Selection method to use.
        crossover : BaseCrossover.
            Crossover method to use.
        history : BaseHistory
            Object to store the history of the optimisation process to.
        termination_manager : BaseTerminationManager
            Manager to determine when termination criteria is met.
        constraint_manager : ConstraintManager
            Manager to determine if imposed constraints are violated.
        """

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

    def step_optimise(self, fn):

        """
        Progresses the optimisation prcedure by a single iteration.

        Parameters
        ----------
        fn : function
            Fitness function used to evaluate the fitness.
        """

        for individual in self.population:
            self.evaluate_fitness(individual, fn)

            if not self.constraint_manager.violates_position(individual):
                self.update_best(individual)

        self.selection.preprocess(self.population)

        _population = []
        for i in range(self.n_individuals // 2):
            parent_a = self.selection.select(self.population)
            parent_b = self.selection.select(self.population)

            child_a, child_b = self.crossover.cross(parent_a, parent_b)

            child_a = self.mutation.mutate(child_a)
            child_b = self.mutation.mutate(child_b)

            _population.extend([child_a, child_b])

        self.population = _population
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

        while not self.termination_manager.termination_check():
            self.step_optimise(fn)
            self.iteration += 1
