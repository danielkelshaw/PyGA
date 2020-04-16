import pytest
from pyga.individual import Individual
from pyga.soga import SOGA


class TestSOGA:

    @pytest.fixture
    def soga(self):

        bounds = {
            'x0': [0.0, 10.0],
            'x1': [0.0, 10.0]
        }

        n_individuals = 10
        n_iterations = 10

        soga = SOGA(bounds, n_individuals, n_iterations)
        return soga

    @pytest.fixture
    def individual(self):
        bounds = {
            'x0': [0.0, 10.0],
            'x1': [0.0, 10.0]
        }

        individual = Individual(bounds)
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

    def test_update_best(self, soga, individual):

        bounds = {
            'x0': [0.0, 10.0],
            'x1': [0.0, 10.0]
        }

        soga.best_individual = Individual(bounds)
        soga.best_individual.fitness = 100.0

        soga.update_best(individual)
        assert soga.best_individual.fitness == 50.0
