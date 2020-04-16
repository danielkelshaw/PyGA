import pytest
import numpy as np
from pyga.individual import Individual


class TestIndividual:

    def test_init(self):

        bounds = {
            'x0': [0, 10],
            'x1': [0, 10]
        }

        individual = Individual(bounds)

        assert isinstance(individual.lb, np.ndarray)
        assert isinstance(individual.ub, np.ndarray)
        assert isinstance(individual.position, np.ndarray)
        assert individual.fitness is None
