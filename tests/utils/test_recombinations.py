import pytest
from pyga.individual import Individual
from pyga.utils.recombinations import *


@pytest.fixture
def parent_a():
    return Individual([0.0, 0.0, 0.0, 0.0], [50.0, 50.0, 50.0, 50.0])


@pytest.fixture
def parent_b():
    return Individual([0.0, 0.0, 0.0, 0.0], [50.0, 50.0, 50.0, 50.0])


class TestLineRecombination:

    @pytest.mark.parametrize('p', [-0.25, 0.25])
    def test_cross(self, parent_a, parent_b, p):

        if p == -0.25:
            with pytest.raises(ValueError):
                recombination = LineRecombination(p=p)

        else:
            recombination = LineRecombination(p=p)
            ret_a, ret_b = recombination.cross(parent_a, parent_b)

            assert isinstance(ret_a, Individual)
            assert isinstance(ret_b, Individual)

    @pytest.mark.parametrize('pos', [[25.0, 25.0], [75.0, 25.0], [75.0, 75.0]])
    def test__in_bounds(self, pos):
        lb, ub = [0.0, 0.0], [50.0, 50.0]
        recombination = LineRecombination()

        if pos == [25.0, 25.0]:
            assert recombination._in_bounds(pos, lb, ub)
        else:
            assert not recombination._in_bounds(pos, lb, ub)


class TestIntermediateRecombination:

    def test_cross(self):
        pass
