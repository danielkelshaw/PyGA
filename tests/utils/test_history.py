import pytest
from pyga.utils.history import *
from pyga.soga import SOGA
from pyga.individual import Individual


class TestGeneralHistory:

    @pytest.fixture
    def soga(self):

        bounds = {
            'x0': [0.0, 10.0],
            'x1': [0.0, 10.0]

        }
        soga = SOGA(bounds, n_individuals=30, n_iterations=100)
        soga.initialise_population()

        soga.best_individual = Individual(bounds)
        soga.best_individual.fitness = 0.5

        for idx, individual in enumerate(soga.population):
            individual.fitness = 5.0

        return soga

    def test_write_history(self, soga):

        hist = GeneralHistory(soga)
        hist.write_history()

        assert isinstance(hist.arr_best_fitness, list)
        assert isinstance(hist.arr_mean_fitness, list)

        assert len(hist.arr_best_fitness) == len(hist.arr_mean_fitness) == 1
        assert hist.arr_best_fitness[0] == 0.5
        assert hist.arr_mean_fitness[0] == 5.0
