import abc


class BaseGA(abc.ABC):

    def __init__(self, bounds, n_individuals):

        """
        Initialiser for the BaseGA class.

        Parameters
        ----------
        bounds : dict
            Lower and upper bounds of the search space.
        n_individuals : int
            Number of individuals for use in the population.

        Attributes
        ----------
        pnames : list
            Parameter names assigned to the bounds.
        population : list
            List of Individuals within the population.
        iteration : int
            Current iteration for the optimisation process.
        """

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

        """
        Responsible for resetting the optimisation environment.

        Raises
        ------
        NotImplementedError
            Method has not yet been implemented.
        """

        raise NotImplementedError('BaseGA::reset_environment()')

    @abc.abstractmethod
    def initialise_population(self):

        """
        Generates the population list of Individuals.

        Raises
        ------
        NotImplementedError
            Method has not yet been implemented.
        """

        raise NotImplementedError('BaseGA::initialise_population()')

    @staticmethod
    @abc.abstractmethod
    def evaluate_fitness(individual, fn):

        """
        Sets the fitness of the individual passed in.

        Parameters
        ----------
        individual : Individual
            Individual for which to assess the fitness.
        fn : function
            Fitness function used to evaluate the fitness.

        Raises
        ------
        NotImplementedError
            Method has not yet been implemented.
        """

        raise NotImplementedError('BaseGA::evaluate_fitness()')

    @abc.abstractmethod
    def step_optimise(self, fn):

        """
        Progresses the optimisation prcedure by a single iteration.

        Parameters
        ----------
        fn : function
            Fitness function used to evaluate the fitness.

        Raises
        ------
        NotImplementedError
            Method has not yet been implemented.
        """

        raise NotImplementedError('BaseGA::step_optimise()')

    @abc.abstractmethod
    def optimise(self, fn):

        """
        Responsible for managing the optimisation process.

        Parameters
        ----------
        fn : function
            Fitness function used to evaluate the fitness.

        Raises
        ------
        NotImplementedError
            Method has not yet been implemented.
        """

        raise NotImplementedError('BaseGA::optimise()')
