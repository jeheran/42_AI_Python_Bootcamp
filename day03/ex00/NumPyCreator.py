import numpy as np
import random


class NumPyCreator:
    def __init__(self, *args):
        pass

    def from_list(self, *args):
        #return np.array(*args, dtype=None, copy=True, order='K', subok=False, ndmin=0)
        return np.array(*args)

    def from_tuple(self, *args):
        return np.array(*args)

    def from_iterable(self, *args):
        return np.array(*args)

    def from_shape(self, shape, value=0):
        return np.full((shape[0], shape[1]), value)

    def random(self, shape):
        return np.random.sample(10) * 5

    def identity(self, n):
        return np.identity(n, dtype=None)

