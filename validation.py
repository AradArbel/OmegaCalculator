from exceptions import InsufficientArguments, ConsecutiveArguments, UnBalancedParenthesis, UnsupportedChar, EmptyInput
from custom_operator import Operator
from expression_utils import remove_spaces, get_next, possible_places, LEGAL_CHARACTERS


def validate_priority(sub_expressions: list, priority) -> list:
    """
    validates operators with this priority
    :param sub_expressions: list of all sub expression
    :param priority: priority to validate operators of
    :return: None
    """
    updated_sub_expressions = []
    i = 0
    while i < len(sub_expressions):
        if type(sub_expressions[i]) is Operator and sub_expressions[i].get_priority() == priority:
            places = possible_places(sub_expressions, i)
            if "middle" in sub_expressions[i].get_places():
                if "middle" not in places and ["middle"] == sub_expressions[i].get_places():
                    raise InsufficientArguments(places, sub_expressions[i].get_sign())
                else:
                    i += 2
                    continue
            if "left" in sub_expressions[i].get_places():
                if "left" not in places and "right" not in sub_expressions[i].get_places():
                    raise InsufficientArguments(places, sub_expressions[i].get_sign())
                else:
                    updated_sub_expressions.append(sub_expressions[i + 1])
                    i += 2
                    continue
            if "right" in sub_expressions[i].get_places():
                if "right" not in places:
                    raise InsufficientArguments(places, sub_expressions[i].get_sign())
                else:
                    if type(updated_sub_expressions[-1]) is not str:
                        updated_sub_expressions.append(sub_expressions[i - 1])
        elif type(sub_expressions[i]) is str:
            if len(updated_sub_expressions) > 0 and type(updated_sub_expressions[-1]) is not Operator:
                raise ConsecutiveArguments
            else:
                updated_sub_expressions.append(sub_expressions[i])
        else:
            updated_sub_expressions.append(sub_expressions[i])
        i += 1
    return updated_sub_expressions[:]


def validate(exp: str) -> None:
    """
    Goes over the expression and raises exception if it is illegal
    :param exp: expression to validate
    :return: None
    """
    if exp == "":
        raise EmptyInput
    exp = remove_spaces(exp)
    if not balanced_parentheses(exp):
        raise UnBalancedParenthesis
    for c in exp:
        if c not in LEGAL_CHARACTERS:
            raise UnsupportedChar(c)
    sub_expressions = []
    position = 0
    while position < len(exp):
        position, sub_exp = get_next(exp, position)
        if type(sub_exp) is str and sub_exp[0] == "(":
            validate(sub_exp[1:-1])
            sub_expressions.append('1')
        else:
            sub_expressions.append(sub_exp)
    for j in range(6, 0, -1):
        sub_expressions = validate_priority(sub_expressions, j)


def balanced_parentheses(exp: str) -> bool:
    """
    validates legal parentheses
    :param exp: expression to validate
    :return: True if parentheses are legal, False otherwise
    """
    balance = 0
    for c in exp:
        if c == "(":
            balance -= 1
        elif c == ")":
            if balance == 0:
                return False
            balance += 1
    return balance == 0

