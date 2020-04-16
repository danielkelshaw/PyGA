import pytest
from pyga.individual import Individual
from pyga.utils.crossovers import *


@pytest.fixture
def parent_a():

    bounds = {
            'x0': [0.0, 10.0],
            'x1': [0.0, 10.0]
    }

    return Individual(bounds)


@pytest.fixture
def parent_b():

    bounds = {
            'x0': [0.0, 10.0],
            'x1': [0.0, 10.0]
    }

    return Individual(bounds)


class TestOnePointCrossover:

    def test_cross(self, parent_a, parent_b):

        crossover = OnePointCrossover()
        ret_a, ret_b = crossover.cross(parent_a, parent_b)

        total_parent_set = set(parent_a.position) | set(parent_b.position)
        total_ret_set = set(ret_a.position) | set(ret_b.position)

        assert total_parent_set == total_ret_set
        assert isinstance(ret_a, Individual)
        assert isinstance(ret_b, Individual)


class TestTwoPointCrossover:

    def test_cross(self, parent_a, parent_b):

        crossover = TwoPointCrossover()
        ret_a, ret_b = crossover.cross(parent_a, parent_b)

        total_parent_set = set(parent_a.position) | set(parent_b.position)
        total_ret_set = set(ret_a.position) | set(ret_b.position)

        assert total_parent_set == total_ret_set
        assert isinstance(ret_a, Individual)
        assert isinstance(ret_b, Individual)


class TestUniformCrossover:

    @pytest.mark.parametrize('p_swap', [0.1, None, 0.7])
    def test_cross(self, parent_a, parent_b, p_swap):

        if p_swap == 0.7:
            with pytest.raises(ValueError):
                crossover = UniformCrossover(p_swap=p_swap)

        else:
            crossover = UniformCrossover(p_swap=p_swap)
            ret_a, ret_b = crossover.cross(parent_a, parent_b)

            total_parent_set = set(parent_a.position) | set(parent_b.position)
            total_ret_set = set(ret_a.position) | set(ret_b.position)

            assert total_parent_set == total_ret_set
            assert isinstance(ret_a, Individual)
            assert isinstance(ret_b, Individual)


class TestKVectorUniformCrossover:

    def test_cross(self):
        pass
