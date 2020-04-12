import pytest
from pyga.individual import Individual
from pyga.soga import SOGA


class TestSOGA:

    @pytest.fixture
    def soga(self):

        lb = [0.0, 0.0]
        ub = [10.0, 10.0]
        n_individuals = 10
        n_iterations = 10

        soga = SOGA(lb, ub, n_individuals, n_iterations)
        return soga

    @pytest.fixture
    def individual(self):

        lb = [0.0, 0.0]
        ub = [10.0, 10.0]

        individual = Individual(lb, ub)
        individual.fitness = 50.0

        return individual

    def test_reset_environment(self, soga, individual):

        soga.iteration = 5
        soga.initialise_population()
        soga.best_individual = individual

        soga.reset_environment()
        assert soga.iteration == 0
        assert soga.population == []
        assert soga.best_individual is None

    def test_initialise_population(self, soga):

        soga.initialise_population()

        assert isinstance(soga.population, list)
        for individual in soga.population:
            assert isinstance(individual, Individual)

        assert len(soga.population) == soga.n_individuals

    @pytest.mark.parametrize('it', [5, 10, 15])
    def test_termination_check(self, soga, it):

        soga.iteration = it
        ret_bool = soga.termination_check()

        if it == 5:
            assert not ret_bool
        elif it == 10:
            assert not ret_bool
        elif it == 15:
            assert ret_bool

    def test_update_best(self, soga, individual):

        lb = [0.0, 0.0]
        ub = [10.0, 10.0]

        soga.best_individual = Individual(lb, ub)
        soga.best_individual.fitness = 100.0

        soga.update_best(individual)
        assert soga.best_individual.fitness == 50.0
