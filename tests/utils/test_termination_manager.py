import pytest
import time
from pyga.soga import SOGA
from pyga.individual import Individual
from pyga.utils.termination_manager import *


@pytest.fixture
def ga():
    lb, ub = [0.0, 0.0], [50.0, 50.0]
    ga = SOGA(lb, ub, n_individuals=10, n_iterations=100)
    return ga


class TestIterationTerminationManager:

    def test_termination_check(self, ga):

        ga.iteration = 150
        tm = IterationTerminationManager(ga)
        ret_bool = tm.termination_check()

        assert ret_bool


class TestTimeTerminationManager:

    def test_termination_check(self):

        tm = TimeTerminationManager(t_budget=1)
        tm.t_start = time.time()
        time.sleep(2)
        ret_bool = tm.termination_check()

        assert ret_bool

class TestEvaluationTerminationManager:

    def test_termination_check(self, ga):

        ga.iteration = 11
        tm = EvaluationTerminationManager(ga, n_evaluations=100)
        ret_bool = tm.termination_check()

        assert ret_bool


class TestErrorTerminationManager:

    def test_termination_check(self, ga):
        best = Individual([0.0, 0.0], [50.0, 50.0])
        best.fitness = 0.0001
        ga.best_individual = best

        tm = ErrorTerminationManager(ga, 0.0, 1e-3)
        ret_bool = tm.termination_check()

        assert ret_bool
