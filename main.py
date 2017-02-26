import argparse
from pprint import pprint

from simplex import Simplex


parser = argparse.ArgumentParser(description="Parser for any url using css-selector.")
parser.add_argument("v_count", type=int, help="count of vars")
parser.add_argument("c_count", type=int, help="count of constraints")
parser.add_argument("g_condition", type=str, choices=['min', 'max'],
                    help="goal condition: minimum or maximum")
args = parser.parse_args()

print("Building goal function...")

goal_function = ''
for i in range(args.v_count):
    s = input("Enter {} coeff for goal function: ".format(i+1))
    goal_function += s + 'x_{}'.format(i+1) + ' + '

goal_function = goal_function[:-3:]
objective = (args.g_condition, goal_function)

print("Building constraints...")

constraints = []
for i in range(args.c_count):
    print("Enter {} constraint...".format(i+1))

    constraint = ''
    for i in range(args.v_count):
        value = input("Enter {} value: ".format(i+1))
        constraint += value + 'x_{}'.format(i+1) + ' + '
    constraint = constraint[:-3:]

    sign = input("Sign ['<=', '=', '>=']: ")
    b = input("Free coeff: ")
    constraint += ' ' + sign + ' ' + b
    constraints.append(constraint)

print("\nYour goal function is: {} -> {}\n".format(goal_function, args.g_condition))
print("Your constraints is: ")
for i in constraints:
    print(i)

Lp_system = Simplex(num_vars=args.v_count, constraints=constraints, objective_function=objective)

print("\nResult: ")
print(Lp_system.solution)
print(Lp_system.optimize_val)
