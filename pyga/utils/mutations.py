import abc
import numpy as np


class BaseMutation(abc.ABC):

    """Abstract Base Class for all Mutation functionality."""

    @abc.abstractmethod
    def mutate(self, individual):

        """
        Mutates the provided individual.

        Parameters
        ----------
        individual : Individual
            Individual for which to mutate.

        Raises
        ------
        NotImplementedError
            This function has not yet been implemented.
        """

        raise NotImplementedError('BaseMutation::mutate()')


class RandomMutation(BaseMutation):

    # TODO >> Improve this definition
    def __init__(self, lower=0.9, upper=1.1):
        self.lower = lower
        self.upper = upper

    def mutate(self, individual):

        """
        Mutates the provided individual.

        Parameters
        ----------
        individual : Individual
            Individual for which to mutate.

        Returns
        -------
        Individual
            Individual with mutated position.
        """

        individual.position *= np.random.uniform(self.lower, self.upper)
        return individual
