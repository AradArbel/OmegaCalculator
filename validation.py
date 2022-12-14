"""
Auther: Arad Arbel
Description: this module contains the validation functions which check if the equation is 
written according to the standard rules.
 """
from exceptions import InsufficientArguments, ConsecutiveArguments, UnBalancedParenthesis, UnsupportedChar, EmptyInput,\
    EmptyBrackets
from custom_operator import Operator
from expression_utils import remove_spaces, get_next, possible_places, LEGAL_CHARACTERS, cancel_minus_signs, \
    WHITE_SPACES


def validate_priority(sub_expressions: list, priority) -> list:
    """
    validates operators with this priority
    :param sub_expressions: list of all sub expression
    :param priority: priority to validate operators of
    :return: None
    """
    updated_sub_expressions = []
    current_place = 0
    while current_place < len(sub_expressions):
        if type(sub_expressions[current_place]) is Operator \
                and sub_expressions[current_place].get_priority() == priority:
            places = possible_places(sub_expressions, updated_sub_expressions, current_place)
            # Check of valid way for sub equation of middle operator
            if "middle" in sub_expressions[current_place].get_places():
                if "middle" not in places and ["middle"] == sub_expressions[current_place].get_places():
                    raise InsufficientArguments(places, sub_expressions[current_place].get_sign())
                elif ["middle"] == sub_expressions[current_place].get_places() :
                    current_place += 2
                    continue
            # Check of valid way for sub equation of left operator
            if "left" in sub_expressions[current_place].get_places():
                if "left" not in places and "right" not in sub_expressions[current_place].get_places():
                    raise InsufficientArguments(places, sub_expressions[current_place].get_sign())
                else:
                    updated_sub_expressions.append(sub_expressions[current_place + 1])
                    current_place += 2
                    continue
            # Check of valid way for sub equation of right operator
            if "right" in sub_expressions[current_place].get_places():
                if "right" not in places:
                    raise InsufficientArguments(places, sub_expressions[current_place].get_sign())
                else:
                    if type(updated_sub_expressions[-1]) is not str:
                        updated_sub_expressions.append(sub_expressions[current_place - 1])
        # Check if each operand came after operator
        elif type(sub_expressions[current_place]) is str:
            if len(updated_sub_expressions) > 0 and type(updated_sub_expressions[-1]) is not Operator:
                raise ConsecutiveArguments
            else:
                updated_sub_expressions.append(sub_expressions[current_place])
        else:
            updated_sub_expressions.append(sub_expressions[current_place])
        current_place += 1
    return updated_sub_expressions[:]


def validate(exp: str) -> None:
    """
    Goes over the expression and raises exception if it is illegal
    :param exp: expression to validate
    :return: None
    """
    for item in WHITE_SPACES:
        if exp == item:
            raise EmptyInput
    exp = remove_spaces(exp)
    for char in exp:
        if char not in LEGAL_CHARACTERS:
            raise UnsupportedChar(char)
    if not balanced_parentheses(exp):
        raise UnBalancedParenthesis
    sub_expressions = __to_sub_expressions(exp)
    for priority_level in range(6, 0, -1):
        sub_expressions = validate_priority(sub_expressions, priority_level)
    if empty_brackets(exp):
        raise EmptyBrackets


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
            if not validate(sub_exp[1:-1]):
                return []
            sub_exps.append('1')
        else:
            sub_exps.append(sub_exp)
    return cancel_minus_signs(sub_exps)


def balanced_parentheses(exp: str) -> bool:
    """
    validates legal parentheses
    :param exp: expression to validate
    :return: True if parentheses are legal, False otherwise
    """
    balance = 0
    for char in exp:
        if char == "(":
            balance -= 1
        elif char == ")":
            if balance == 0:
                return False
            balance += 1
    return balance == 0


def empty_brackets(exp: str) -> bool:
    """
    validates brackets with content
    :param exp: expression to validate
    :return: True if brackets are not empty, False otherwise
    """
    for char in range(len(exp)):
        if exp[char] == "(" and exp[char + 1] == ")":
            return True
    return False
