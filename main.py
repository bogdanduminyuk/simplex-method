import argparse

from lib.simplex_realization import SimplexRealization


def init_args():
    parser = argparse.ArgumentParser(description="Parser for any url using css-selector.")
    parser.add_argument("v_count", type=int, help="count of vars")
    parser.add_argument("c_count", type=int, help="count of constraints")
    parser.add_argument("g_condition", type=str, choices=['min', 'max'],
                        help="goal condition: minimum or maximum")
    return parser.parse_args()


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

    Lp_system = SimplexRealization(args.v_count, args.c_count,
                                   args.g_condition, coeffs, constraints_coeffs,
                                   signs, free_coeffs)

    print("\nResult: ")
    print(Lp_system.solution)
    print(Lp_system.optimize_val)
