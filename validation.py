import exceptions
from operatorx import OperatorX


LEGAL_CHARS = "1234567890+-*/^%$&@~!#.()"
OPERATORS = "+-*/^%$&@~!#"


def validate(exp: str):
    exp = "".join(exp.split(" "))
    if not balanced_parentheses(exp):
        raise exceptions.UnBalancedParenthesis
    for c in exp:
        if c not in LEGAL_CHARS:
            raise Exception("todo change this")
    position = 0
    sub_exps = []
    updated_sub_exps = []
    while position < len(exp):
        position, sub_exp = get_next(exp, position)
        sub_exps.append(sub_exp)
    for j in range(6, 0, -1):
        for i in range(len(sub_exps)):
            if type(sub_exps[i]) is OperatorX and sub_exps[i].get_priority() == j:
                if sub_exps[i].get_place() == "left":
                    if i == len(sub_exps) - 1 or type(sub_exps[i+1]) is not str:
                        raise Exception(f"Error: operator {sub_exps[i].get_sign()} must have argument to the right")
                    else:
                        updated_sub_exps.append(sub_exps[i+1])
                if sub_exps[i].get_place() == "right":
                    if i == 0 or type(sub_exps[i-1]) is not str:
                        raise Exception(f"Error: operator {sub_exps[i].get_sign()} must have argument to the left")
                    else:
                        if type(updated_sub_exps[-1]) is not str:
                            updated_sub_exps.append(sub_exps[i-1])
                if sub_exps[i].get_place() == "middle":
                    if i == 0 or i == len(sub_exps) - 1 or type(sub_exps[i+1]) is not str or type(sub_exps[i-1]) is not str:
                        raise Exception(f"Error: operator {sub_exps[i].get_sign()} must have argument to the right and to the left")
                    else:
                        updated_sub_exps.append(sub_exps[i+1])
            else:
                if len(updated_sub_exps) > 0 and type(updated_sub_exps[-1]) is not OperatorX:
                    raise Exception("Error: consecutive arguments without binary operator between them")
                else:
                    updated_sub_exps.append(sub_exps[i])
        sub_exps = updated_sub_exps[:]


def get_next(exp: str, position: int):
    if exp[position] in OPERATORS:
        return position + 1, OperatorX(exp[position])
    i = position
    s = ""
    while i < len(exp) and exp[i] not in OPERATORS:
        s += exp[i]
        i += 1
    return i, s


def balanced_parentheses(exp: str):
    balance = 0
    for c in exp:
        if c == "(":
            balance -= 1
        elif c == ")":
            if balance > 0:
                return False
            balance += 1
    return balance == 0

try:
    validate("))))))")
except Exception as e:
    print(e)
