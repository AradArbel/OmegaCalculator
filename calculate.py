import operators
from custom_operator import Operator, OPERATORS_NAME
from expression_utils import remove_spaces, get_next, possible_places

"""
Auther: Arad Arbel
Description: this module contains the calculate functions which solving the equation using all the helper functions below.
"""


def calculate(exp: str) -> float:
    """
    evaluates the expression given
    :param exp: the expression
    :return: the evaluation of the expression
    """
    exp = remove_spaces(exp)
    if exp[0] == '-' and len(exp) > 1 and exp[1] != "(":
        return calculate("-(" + exp[1:] + ")")
    sub_expressions = __to_sub_expressions(exp)
    for priority in range(6, 0, -1):
        sub_expressions = __calculate_priority(sub_expressions, priority)
    return sub_expressions[0]


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
    return __cancel_minus_signs(sub_exps)


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
            places = possible_places(sub_exps, current_length)
            if "middle" in places and "middle" in sub_exps[current_length].get_places():
                updated_sub_exps[-1] = (op_func(updated_sub_exps[-1], sub_exps[current_length + 1]))
                current_length += 2
                continue
            if "left" in places and "left" in sub_exps[current_length].get_places():
                if sub_exps[current_length].get_sign() == '-':
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


def __join_to_minus(sub_exps, updated_sub_exps, start):
    """
    checks whether sub_exps[start] should be joined with a previous minus sign
    :param sub_exps: sub expressions that contain the number to be checked
    :param updated_sub_exps: a list containing the partial sub expressions updated list
    :param start: the index of the number to be checked
    :return:
    """
    if type(sub_exps[start]) is Operator:
        return False
    if len(updated_sub_exps) < 2:
        return False
    if type(updated_sub_exps[-1]) is not Operator:
        return False
    if updated_sub_exps[-1].get_sign() != '-':
        return False
    if type(updated_sub_exps[-2]) is not Operator:
        return False
    return True


def __cancel_minus_signs(sub_exps: list) -> list:
    """
    :param sub_exps: sub expressions to cancel minuses from
    :return: sub expressions without the canceled minuses
    """
    lst = []
    start = 0
    while start < len(sub_exps):
        if type(sub_exps[start]) is Operator and sub_exps[start].get_sign() == '-':  # beginning of a minus sequence
            num_minuses = 0
            curr = start
            while curr < len(sub_exps) and type(sub_exps[curr]) is Operator and sub_exps[curr].get_sign() == '-':
                num_minuses += 1
                curr += 1
            if start == 0:  # if minus sequence is from beginning
                if num_minuses % 2 == 1:  # if odd number of minuses then put a minus, else skip
                    lst.append(Operator('-'))
            else:
                if num_minuses % 2 == 1:  # if odd number of minuses then put a minus, else put a plus
                    lst.append(Operator('-'))
                elif type(lst[-1]) is not Operator:
                    lst.append(Operator('+'))
            start = curr
        else:  # other sub expressions join to previous minus or add as is if
            if __join_to_minus(sub_exps, lst, start):
                lst[-1] = str(-1 * float(sub_exps[start]))
            else:
                lst.append(sub_exps[start])
            start += 1
    return lst
