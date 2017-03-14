from .simplex import Simplex


class SimplesRealization(Simplex):
    def __init__(self, num_vars, constraints, objective_function):

        super(SimplesRealization, self).__init__(num_vars, constraints, objective_function)