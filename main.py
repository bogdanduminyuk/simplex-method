import argparse

from simplex import Simplex


def init_args():
    parser = argparse.ArgumentParser(description="Parser for any url using css-selector.")
    parser.add_argument("v_count", type=int, help="count of vars")
    parser.add_argument("c_count", type=int, help="count of constraints")
    parser.add_argument("g_condition", type=str, choices=['min', 'max'],
                        help="goal condition: minimum or maximum")
    return parser.parse_args()


def build_objective(num_vars, condition, _coeffs):
    _goal_func = ''

    for _i in range(num_vars):
        _goal_func += _coeffs[_i] + 'x_{}'.format(_i+1) + ' + '
    _goal_func = _goal_func[:-3:]

    return condition, _goal_func


def build_constraints(num_vars, constraints_count, constraint_coeffs, signs, free_coeffs):
    _constraints = []

    for _i in range(constraints_count):
        _constraint = ''

        for j in range(num_vars):
            _constraint += constraint_coeffs[_i][j] + 'x_{}'.format(j+1) + ' + '

        _constraint = _constraint[:-3:]
        _constraint += ' ' + signs[_i] + ' ' + free_coeffs[_i]
        _constraints.append(_constraint)

    return _constraints


if __name__ == "__main__":
    args = init_args()

    print("Building goal function...")
    coeffs = []

    for i in range(args.v_count):
        coeff = input("Enter {} coeff of goal function: ".format(i+1))
        coeffs.append(coeff)

    print("Building constraints...")

    constraints_coeffs, signs, free_coeffs = [], [], []
    for i in range(args.c_count):
        constraint_coeffs = []

        for j in range(args.v_count):
            coeff = input("Enter {} coeff of {} constraint: ".format(i+1, i+1))
            constraint_coeffs.append(coeff)

        signs.append(input("Enter sing[<=, =, >=]: "))
        free_coeffs.append(input("Enter free coeff: "))

        constraints_coeffs.append(constraint_coeffs)

    objective = build_objective(args.v_count, args.g_condition, coeffs)
    constraints = build_constraints(args.v_count, args.c_count, constraints_coeffs, signs, free_coeffs)

    print("\nYour goal function is: {} -> {}\n".format(objective[1], objective[0]))
    print("Your constraints is: ")
    for i in constraints:
        print(i)

    Lp_system = Simplex(num_vars=args.v_count, constraints=constraints, objective_function=objective)

    print("\nResult: ")
    print(Lp_system.solution)
    print(Lp_system.optimize_val)
