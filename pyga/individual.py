import numpy as np


class Individual:

    def __init__(self, bounds):

        """
        Class containing information about a population member.

        Parameters
        ----------
        bounds : dict
            Parameter names mapped to upper / lower bounds.

        Attributes
        ----------
        _pnames : list
            Names assigned to the input bounds.
        position : np.ndarray
            Current position of the individual.
        fitness : float
            Fitness evaluation for the associated position.
        """

        if not isinstance(bounds, dict):
            raise TypeError('bounds must be dict.')

        self._pnames = list(bounds.keys())
        _bounds = np.asarray(list(bounds.values()))

        self.lb = _bounds[0, :]
        self.ub = _bounds[1, :]

        self.position = np.random.uniform(self.lb, self.ub)
        self.fitness = None

    def __str__(self):

        message = 'Position = {\n'

        for k, v in zip(self._pnames, self.position):
            message += f'\t{k:<15}{v}\n'

        message += '}\n'
        message += f'\nFitness = {self.fitness}'

        return message
