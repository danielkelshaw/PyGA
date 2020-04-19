import pytest
import numpy as np

from pyga.individual import Individual
from pyga.utils.mutations import RandomMutation


class TestRandomMutation:

    @pytest.fixture
    def individual(self):

        bounds = {
            'x0': [0.0, 20.0],
            'x1': [0.0, 20.0]
        }

        ind = Individual(bounds)
        ind.position = np.array([10.0, 10.0])

        return ind

    def test_mutate(self, individual):

        mutation = RandomMutation()
        ret_ind = mutation.mutate(individual)

        assert all(ret_ind.position >= 9.0)
        assert all(ret_ind.position <= 11.0)
        assert not np.array_equal(np.array([10.0, 10.0]), ret_ind.position)
