# coding: utf-8

from .simplex import Simplex


class Dual(Simplex):
    def __init__(self, num_vars, constraints, objective_function):
        # do smth
        super(Dual, self).__init__(num_vars, constraints, objective_function)
