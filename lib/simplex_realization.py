from lib.simplex import Simplex


class SimplexRealization(Simplex):
    def __init__(self, num_vars, num_constraints, condition, function_coeffs, var_coeffs, signs, free_coeffs):
        objective_function = SimplexRealization.build_objective(num_vars, condition, function_coeffs)
        constraints = SimplexRealization.build_constraints(num_vars, num_constraints, var_coeffs, signs, free_coeffs)
        print("\nYour goal function is: {} -> {}\n".format(objective_function[1], objective_function[0]))
        print("Your constraints is: ")
        for i in constraints:
            print(i)
        import time
        time.sleep(1)
        super(SimplexRealization, self).__init__(num_vars, constraints, objective_function)

    @staticmethod
    def build_objective(num_vars, condition, _coeffs):
        _goal_func = ''

        for _i in range(num_vars):
            _goal_func += str(_coeffs[_i]) + 'x_{}'.format(_i+1) + ' + '
        _goal_func = _goal_func[:-3:]

        return condition, _goal_func

    @staticmethod
    def build_constraints(num_vars, constraints_count, constraint_coeffs, signs, free_coeffs):
        _constraints = []

        for _i in range(constraints_count):
            _constraint = ''

            for j in range(num_vars):
                _constraint += str(constraint_coeffs[_i][j]) + 'x_{}'.format(j + 1) + ' + '

            _constraint = _constraint[:-3:]
            _constraint += ' ' + signs[_i] + ' ' + str(free_coeffs[_i])
            _constraints.append(_constraint)

        return _constraints


if __name__ == "__main__":
    n_vars = 2
    n_count = 4
    goal = "min"

    function_coeffs = [1, 2]
    vars_coeffs = [
        [0, 1],
        [1, 0],
        [1, -2],
        [-1, 1],
    ]

    signs = [">=", ">=", ">=", ">="]
    free_coeffs = [1, 4, 4, 1]

    Lp_system = SimplexRealization(n_vars, n_count, goal, function_coeffs, vars_coeffs, signs, free_coeffs)

    print("\nResult: ")
    print(Lp_system.solution)
    print(Lp_system.optimize_val)