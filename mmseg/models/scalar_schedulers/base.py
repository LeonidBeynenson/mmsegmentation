from abc import ABCMeta, abstractmethod


class BaseScalarScheduler(metaclass=ABCMeta):
    def __init__(self):
        super(BaseScalarScheduler, self).__init__()

    def __call__(self, step, epoch_size):
        return self._get_value(step, epoch_size)

    @abstractmethod
    def _get_value(self, step, epoch_size):
        pass
