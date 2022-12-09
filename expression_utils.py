from custom_operator import Operator, OPERATORS_NAME
from exceptions import TooManyDecimalPoints

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
    i = position
    s = ""
    decimal_points = 0
    if exp[i] == "(":
        while i < len(exp) and exp[i] != ")":
            s += exp[i]
            i += 1
        s += exp[i]
        return i+1, s
    while i < len(exp) and exp[i] not in OPERATORS_NAME.keys():
        if exp[i] == ".":
            decimal_points += 1
        if decimal_points > 1:
            raise TooManyDecimalPoints
        s += exp[i]
        i += 1
    return i, s


def possible_places(sub_expressions, i):
    """
    calculates a list containing all possible places the operator in sub_exps[i] can have by checking
    the surrounding elements
    :param sub_expressions: sub expressions list that contains the expression to be checked
    :param i: the index of the expression to be checked
    :return: the list of possible places
    """
    places = []
    if i > 0 and type(sub_expressions[i - 1]) is not Operator:
        places.append("right")
    if i < len(sub_expressions) - 1 and type(sub_expressions[i + 1]) is not Operator:
        places.append("left")
    if places == ["right", "left"]:
        places.append("middle")
    return places
