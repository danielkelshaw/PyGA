import numpy as np


class Individual:

    def __init__(self, lb, ub):

        """
        Class containing information about a population member.

        Parameters
        ----------
        lb : list or np.ndarray
            Lower bound of the search space.
        ub : list or np.ndarray
            Upper bound of the search space.

        Attributes
        ----------
        position : np.ndarray
            Current position of the individual.
        fitness : float
            Fitness evaluation for the associated position.
        """

        if len(lb) != len(ub):
            raise ValueError(f'len(lb): {len(lb)} != len(ub): {len(ub)}')

        self.lb = np.asarray(lb)
        self.ub = np.asarray(ub)

        self.position = np.random.uniform(lb, ub)
        self.fitness = None
