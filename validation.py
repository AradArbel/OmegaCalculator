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
        if type(sub_exp) is str and sub_exp[0] == "(":
            validate(sub_exp[1:-1])
            sub_exps.append('1')
        else:
            sub_exps.append(sub_exp)
    for j in range(6, 0, -1):
        i = 0
        while i < len(sub_exps):
            if type(sub_exps[i]) is OperatorX and sub_exps[i].get_priority() == j:
                if "middle" in sub_exps[i].get_places():
                    if (i == 0 or i == len(sub_exps) - 1 or type(sub_exps[i+1]) is not str or type(sub_exps[i-1]) is not str) and \
                            "left" not in sub_exps[i].get_places() and "right" not in sub_exps[i].get_places():
                            raise Exception(f"Error: operator {sub_exps[i].get_sign()} must have argument to the right and to the left")
                    else:
                        i += 2
                        continue
                if "left" in sub_exps[i].get_places():
                    if (i == len(sub_exps) - 1 or type(sub_exps[i+1]) is not str) and "right" not in sub_exps[i].get_places():
                            raise Exception(f"Error: operator {sub_exps[i].get_sign()} must have argument to the right")
                    else:
                        updated_sub_exps.append(sub_exps[i+1])
                        continue
                if "right" in sub_exps[i].get_places():
                    if i == 0 or type(sub_exps[i-1]) is not str:
                        raise Exception(f"Error: operator {sub_exps[i].get_sign()} must have argument to the left")
                    else:
                        if type(updated_sub_exps[-1]) is not str:
                            updated_sub_exps.append(sub_exps[i-1])

            elif type(sub_exps[i]) is str:
                if len(updated_sub_exps) > 0 and type(updated_sub_exps[-1]) is not OperatorX:
                    raise Exception("Error: consecutive arguments without binary operator between them")
                else:
                    updated_sub_exps.append(sub_exps[i])
            else:
                updated_sub_exps.append(sub_exps[i])
            i += 1
        sub_exps = updated_sub_exps[:]
        updated_sub_exps = []


def get_next(exp: str, position: int):
    if exp[position] in OPERATORS:
        return position + 1, OperatorX(exp[position])
    i = position
    s = ""
    if exp[i] == "(":
        while i < len(exp) and exp[i] != ")":
            s += exp[i]
            i += 1
        s += exp[i]
        return i+1, s
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

