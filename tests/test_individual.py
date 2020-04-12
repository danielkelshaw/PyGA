import pytest
import numpy as np
from pyga.individual import Individual


class TestIndividual:

    @pytest.mark.parametrize('ub', [[10, 10], np.array([10, 10])])
    def test_init(self, ub):

        lb = [0, 0]
        individual = Individual(lb, ub)

        assert isinstance(individual.lb, np.ndarray)
        assert isinstance(individual.ub, np.ndarray)
        assert isinstance(individual.position, np.ndarray)
        assert individual.fitness is None

    def test_init_raise(self):

        lb = [0, 0]
        ub = [10, 10, 10]

        with pytest.raises(ValueError):
            individual = Individual(lb, ub)
