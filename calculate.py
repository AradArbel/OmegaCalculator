import operators
from custom_operator import Operator, OPERATORS_NAME
from expression_utils import remove_spaces, get_next, possible_places, cancel_minus_signs

"""
Auther: Arad Arbel
Description: this module contains the functions which solving the equation using all the helper functions below.
"""


def calculate(exp: str) -> float:
    """
    evaluates the expression given
    :param exp: the expression
    :return: the evaluation of the expression
    """
    exp = remove_spaces(exp)
    sub_expressions = __to_sub_expressions(exp)
    for priority in range(6, 0, -1):
        sub_expressions = __calculate_priority(sub_expressions, priority)
    return float(sub_expressions[0])


# ------------------------------ HELPER FUNCTIONS ------------------------------


def __to_sub_expressions(exp: str) -> list:
    """
    splits an expression to sub expressions
    :param exp: original expression
    :return: a list of the sub expressions
    """
    sub_exps = []
    position = 0
    while position < len(exp):
        position, sub_exp = get_next(exp, position)
        if type(sub_exp) is str and sub_exp[0] == "(":
            c = calculate(sub_exp[1:-1])
            sub_exps.append(c)
        else:
            sub_exps.append(sub_exp)
    return cancel_minus_signs(sub_exps)


def __calculate_priority(sub_exps, priority):
    """
    evaluates all operators from sub_exps that hove this priority
    :param sub_exps: a list of sub expressions to evaluate
    :param priority: the priority currently evaluated
    :return: the evaluated sub expressions
    """
    updated_sub_exps = []
    current_length = 0
    while current_length < len(sub_exps):
        if type(sub_exps[current_length]) is Operator and sub_exps[current_length].get_priority() == priority:
            op_func = getattr(operators, OPERATORS_NAME[sub_exps[current_length].get_sign()])
            places = possible_places(sub_exps, updated_sub_exps, current_length)
            if "middle" in places and "middle" in sub_exps[current_length].get_places():
                updated_sub_exps[-1] = (op_func(updated_sub_exps[-1], sub_exps[current_length + 1]))
                current_length += 2
                continue
            if "left" in places and "left" in sub_exps[current_length].get_places():
                if sub_exps[current_length].get_sign() == '-':
                    if str(sub_exps[current_length + 1])[0] == '-':
                        updated_sub_exps.append(str(sub_exps[current_length + 1])[1:])
                    else:
                        updated_sub_exps.append('-' + str(sub_exps[current_length + 1]))
                else:
                    updated_sub_exps.append(op_func(sub_exps[current_length + 1]))
                current_length += 2
                continue
            if "right" in places and "right" in sub_exps[current_length].get_places():
                updated_sub_exps[-1] = op_func(updated_sub_exps[-1])
        else:
            updated_sub_exps.append(sub_exps[current_length])
        current_length += 1
    return updated_sub_exps[:]





