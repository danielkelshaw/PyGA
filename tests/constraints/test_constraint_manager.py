import pytest
import numpy as np

from pyga.soga import SOGA
from pyga.individual import Individual
from pyga.constraints.base_constraints import PositionConstraint
from pyga.constraints.constraint_manager import ConstraintManager


class TestConstraintManager:

    @pytest.fixture
    def soga(self):

        bounds = {
            'x0': [0.0, 10.0],
            'x1': [0.0, 10.0]
        }

        ga = SOGA(bounds, n_individuals=10, n_iterations=10)

        return ga

    @pytest.fixture
    def individual(self):

        ind = Individual({'x0': [0.0, 10.0], 'x1': [0.0, 10.0]})
        ind.position = np.array([2.0, 7.0])

        return ind

    @pytest.fixture
    def position_constraint(self):

        class Constraint(PositionConstraint):

            def constrain(self, position):
                return position['x0'] < 5.0 and position['x1'] > 5.0

        return Constraint()

    def test_violates_position(self, individual, position_constraint, soga):

        cm = ConstraintManager(soga)
        cm.register_constraint(position_constraint)

        assert not cm.violates_position(individual)

    def test_register_constraint(self, position_constraint, soga):

        cm = ConstraintManager(soga)
        cm.register_constraint(position_constraint)

        assert len(cm.constraints) == 1
