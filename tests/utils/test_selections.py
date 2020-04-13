import pytest
from pyga.individual import Individual
from pyga.utils.selections import *


@pytest.fixture
def population():

    population = []
    for i in range(1, 5 + 1):
        _ind = Individual([0], [10])
        _ind.fitness = i
        population.append(_ind)

    return population


class TestRandomSelection:

    def test_select(self, population):

        selection = RandomSelection()
        selection.preprocess(population)
        ret_ind = selection.select(population)

        assert isinstance(ret_ind, Individual)


class TestTournamentSelection:

    @pytest.mark.parametrize('t', [0, 2, 5])
    def test_select(self, population, t):

        if t == 0:
            with pytest.raises(ValueError):
                selection = TournamentSelection(t_size=t)
        else:
            selection = TournamentSelection(t_size=t)
            selection.preprocess(population)
            ret_int = selection.select(population)

            assert isinstance(ret_int, Individual)


class TestFitnessProportionateSelection:

    def test_preprocess(self, population):

        cdf_sum = sum([1 / i.fitness for i in population])
        selection = FitnessProportionateSelection()
        selection.preprocess(population)

        assert selection.cdf[-1] == cdf_sum
        assert isinstance(selection.cdf, list)

    def test_select(self, population):

        selection = FitnessProportionateSelection()
        selection.preprocess(population)
        ret_ind = selection.select(population)

        assert isinstance(ret_ind, Individual)


class TestStochasticUniversalSamplingSelection:

    def test_preprocess(self, population):

        cdf_sum = sum([1 / i.fitness for i in population])
        selection = StochasticUniversalSamplingSelection()
        selection.preprocess(population)

        assert selection.cdf[-1] == cdf_sum
        assert isinstance(selection.cdf, list)
        assert isinstance(selection.population, list)
        for ind in selection.population:
            assert isinstance(ind, Individual)

    def test_select(self, population):

        selection = StochasticUniversalSamplingSelection()
        selection.preprocess(population)
        ret_ind = selection.select(population)

        assert isinstance(ret_ind, Individual)

    def test__shuffle(self, population):

        pre_set = set([i.fitness for i in population])

        selection = StochasticUniversalSamplingSelection()
        ret_pop = selection._shuffle(population)

        post_set = set([i.fitness for i in ret_pop])

        assert pre_set == post_set
        assert isinstance(ret_pop, list)
        for ind in ret_pop:
            assert isinstance(ind, Individual)
