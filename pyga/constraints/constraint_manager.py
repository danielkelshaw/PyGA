from .base_constraints import BaseConstraint, PositionConstraint


class ConstraintManager:

    def __init__(self, ga):

        """
        Initialiser for ConstraintManager.

        Parameters
        ----------
        ga : SOGA
            Instance of SOGA to be used.
        """

        self.ga = ga
        self.constraints = []

    def violates_position(self, individual):

        """
        Checks if position constraints have been violated.

        Parameters
        ----------
        individual : Individual
            The individual for which to check the constraints.

        Returns
        -------
        bool
            True if position constraints are violated, False otherwise.
        """

        position = dict(zip(self.ga.pnames, individual.position))

        within_constraints = True
        for constraint in self.constraints:
            if isinstance(constraint, PositionConstraint):
                within_constraints = constraint.constrain(position)

            if not within_constraints:
                return True

        return False

    def register_constraint(self, constraint):

        """
        Adds a constraint to be tested.

        Parameters
        ----------
        constraint : BaseConstraint
            The constraint to check.
        """

        if not isinstance(constraint, BaseConstraint):
            raise TypeError('constraint must inherit from BaseConstraint')

        self.constraints.append(constraint)
