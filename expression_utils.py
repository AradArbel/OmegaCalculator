from custom_operator import Operator, OPERATORS_NAME
from exceptions import TooManyDecimalPoints

"""
Auther: Arad Arbel
Description: this module contains utility functions that handle the equations.
 """

LEGAL_CHARACTERS = "1234567890()." + "".join(OPERATORS_NAME.keys())


def remove_spaces(exp: str) -> str:
    """
    removes spaces from an expression
    :param exp: original expression
    :return: the expression without spaces
    """
    return "".join(exp.split(" "))


def get_next(exp: str, position: int) -> tuple:
    """
    gets the next sub expression
    :param exp: expression to serach in
    :param position: start position to search
    :return: (position after the sub expression, the sub expression)
    """
    if exp[position] in OPERATORS_NAME.keys():
        return position + 1, Operator(exp[position])
    current_position = position
    s = ""
    decimal_points = 0
    if exp[current_position] == "(":
        balance = 0
        while current_position < len(exp) and exp[current_position] != ")" or balance < -1:
            if exp[current_position] == "(":
                balance -= 1
            elif exp[current_position] == ")":
                balance += 1
            s += exp[current_position]
            current_position += 1
        s += exp[current_position]
        return current_position+1, s
    while current_position < len(exp) and exp[current_position] not in OPERATORS_NAME.keys():
        if exp[current_position] == ".":
            decimal_points += 1
        if decimal_points > 1:
            raise TooManyDecimalPoints
        s += exp[current_position]
        current_position += 1
    return current_position, s


def possible_places(sub_expressions, updated_sub_expressions, place):
    """
    calculates a list containing all possible places the operator in sub_exps[place] can have by checking
    the surrounding elements
    :param updated_sub_expressions: partially parsed expressions
    :param sub_expressions: sub expressions list that contains the expression to be checked
    :param place: the index of the expression to be checked
    :return: the list of possible places
    """
    places = []
    if place > 0 and type(updated_sub_expressions[-1]) is not Operator:
        places.append("right")
    if place < len(sub_expressions) - 1 and type(sub_expressions[place + 1]) is not Operator:
        places.append("left")
    if places == ["right", "left"]:
        places.append("middle")
    return places


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
    if len(updated_sub_exps) == 0:
        return False
    if type(updated_sub_exps[-1]) is not Operator:
        return False
    if updated_sub_exps[-1].get_sign() != '-':
        return False
    if len(updated_sub_exps) > 1 and type(updated_sub_exps[-2]) is not Operator:
        return False
    return True


def cancel_minus_signs(sub_exps: list) -> list:
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


