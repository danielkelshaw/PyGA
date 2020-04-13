import pytest
from pyga.individual import Individual
from pyga.utils.recombinations import *


@pytest.fixture
def parent_a():
    return Individual([0.0, 0.0, 0.0, 0.0], [50.0, 50.0, 50.0, 50.0])


@pytest.fixture
def parent_b():
    return Individual([0.0, 0.0, 0.0, 0.0], [50.0, 50.0, 50.0, 50.0])


class TestBaseRecombination:

    def test_init_raise(self):
        with pytest.raises(ValueError):
            recombination = BaseRecombination(p=-0.25)

    @pytest.mark.parametrize('pos', [[25.0, 25.0], [75.0, 25.0], [75.0, 75.0]])
    def test__in_bounds(self, pos):
        lb, ub = [0.0, 0.0], [50.0, 50.0]
        recombination = BaseRecombination(p=0.25)

        if pos == [25.0, 25.0]:
            assert recombination._in_bounds(pos, lb, ub)
        else:
            assert not recombination._in_bounds(pos, lb, ub)


class TestLineRecombination:

    def test_cross(self, parent_a, parent_b):
        recombination = LineRecombination()
        ret_a, ret_b = recombination.cross(parent_a, parent_b)

        assert isinstance(recombination, (BaseRecombination, BaseCrossover))
        assert isinstance(ret_a, Individual)
        assert isinstance(ret_b, Individual)


class TestIntermediateRecombination:

    def test_cross(self, parent_a, parent_b):
        recombination = LineRecombination()
        ret_a, ret_b = recombination.cross(parent_a, parent_b)

        assert isinstance(recombination, (BaseRecombination, BaseCrossover))
        assert isinstance(ret_a, Individual)
        assert isinstance(ret_b, Individual)
