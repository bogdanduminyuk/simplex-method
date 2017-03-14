# coding: utf-8
import numpy as np

from lib.simplex_realization import SimplexRealization


class Dual(SimplexRealization):
    def __init__(self, num_vars, num_constraints, condition, function_coeffs, var_coeffs, signs, free_coeffs):
        new_n_vars = num_constraints
        new_n_constraints = num_vars

        new_function_coeffs = free_coeffs
        new_free_coeffs = function_coeffs
        new_var_coeffs = np.matrix(var_coeffs).getT().tolist()

        new_signs = Dual.get_new_signs(condition, signs, num_constraints, new_n_constraints)

        if condition == "max":
            condition = "min"
        elif condition == "min":
            condition = "max"

        super(Dual, self).__init__(new_n_vars, new_n_constraints,
                                   condition, new_function_coeffs, new_var_coeffs,
                                   new_signs, new_free_coeffs)

    @staticmethod
    def get_new_signs(goal, signs, old_num_constraints, new_num_constraints):
        if goal == "max":
            if signs == ["<=" for i in range(old_num_constraints)] or signs == ["=" for i in range(old_num_constraints)]:
                return [">=" for i in range(new_num_constraints)]

        if goal == "min":
            if signs == [">=" for i in range(old_num_constraints)] or signs == ["=" for i in range(old_num_constraints)]:
                return ["<=" for i in range(new_num_constraints)]


if __name__ == "__main__":
    num_vars = 4
    num_constraints = 2
    condition = "max"
    function_coeffs = [2, 4, 4, 1]
    var_coeffs = [
        [0, 1, 1, -1],
        [2, 0, -2, 1],
    ]
    signs = ["=", "="]
    free_coeffs = [1, 2]

    task = Dual(num_vars, num_constraints, condition, function_coeffs, var_coeffs, signs, free_coeffs)
    print("\nResult: ")
    print(task.solution)
    print(task.optimize_val)