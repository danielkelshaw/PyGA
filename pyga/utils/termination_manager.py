import abc
import time


class BaseTerminationManager(abc.ABC):

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @abc.abstractmethod
    def termination_check(self):
        raise NotImplementedError(
            'BaseTerminationManager::termination_check()'
        )


class IterationTerminationManager(BaseTerminationManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def termination_check(self):
        raise NotImplementedError(
            'IterationTerminationManager::termination_check()'
        )


class TimeTerminationManager(BaseTerminationManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def termination_check(self):
        raise NotImplementedError(
            'TimeTerminationManager::termination_check()'
        )


class ErrorTerminationManager(BaseTerminationManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def termination_check(self):
        raise NotImplementedError(
            'ErrorTerminationManager::termination_check()'
        )
