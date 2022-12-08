import operators
import operatorx
from operatorx import OperatorX
from validation import get_next

# todo clean spaces, support more than one digit, validation, exceptions
# (...) operator (...) / (...) operator / operator (...) / ....
def sub_expression(exp: str, start: int):
    if exp[start] == "(":
        i = start + 1
        while i < len(exp):
            if exp[i] == ")":
                return start+1, i+1, exp[start+1:i]
            i += 1
    else:
        i = start + 1
        while i < len(exp):
            if exp[i] in operators.operators_signs.keys():
                return start, i, exp[start:i]
            i += 1
        return start, len(exp), exp[start:]

def calculate(exp: str) -> float:
    position = 0
    sub_exps = []
    updated_sub_exps = []
    # while position < len(exp):
    #     position, sub_exp = get_next(exp, position)
    #     sub_exps.append(sub_exp)
    while position < len(exp):
        position, sub_exp = get_next(exp, position)
        if type(sub_exp) is str and sub_exp[0] == "(":
            c = calculate(sub_exp[1:-1])
            sub_exps.append(c)
        else:
            sub_exps.append(sub_exp)
    for j in range(6, 0, -1):
        i = 0
        while i < len(sub_exps):
            if type(sub_exps[i]) is OperatorX and sub_exps[i].get_priority() == j:
                op_func = getattr(operators, operators.operators_signs[sub_exps[i].get_sign()])
                if "middle" in sub_exps[i].get_places() and (
                        0 < i < len(sub_exps) - 1 and type(sub_exps[i + 1]) is not OperatorX and type(sub_exps[i - 1]) is not OperatorX):
                    updated_sub_exps[-1] = (op_func(updated_sub_exps[-1], sub_exps[i + 1]))
                    i += 2
                    continue

                if "left" in sub_exps[i].get_places():
                    if (i == len(sub_exps) - 1 or type(sub_exps[i + 1]) is not str) and "right" not in sub_exps[i].get_places():
                        raise Exception(f"Error: operator {sub_exps[i].get_sign()} must have argument to the right")
                    else:
                        if sub_exps[i].get_sign() == '-':
                            if sub_exps[i+1].get_sign() == '-':

                            updated_sub_exps.append('-' + str(sub_exps[i + 1]))
                            i += 1
                        else:
                            updated_sub_exps.append(op_func(sub_exps[i+1]))
                        i += 1
                        continue
                if "right" in sub_exps[i].get_places():
                    if i == 0 or type(sub_exps[i - 1]) is not str:
                        raise Exception(f"Error: operator {sub_exps[i].get_sign()} must have argument to the left")
                    else:
                        if type(updated_sub_exps[-1]) is not str:
                            updated_sub_exps[-1] = op_func(updated_sub_exps[i - 1])
                            i += 1

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
    return sub_exps[0]
    # balance = 0
    # operands_lst = []  # [3,4,5]
    # operators_lst = []  # ['+', '*']
    # i = 0
    # while i < len(exp):
    #     if exp[i] in operators.operators_signs.keys() and balance == 0:
    #         operators_lst.append(operatorx.OperatorX(exp[i]))
    #         i += 1
    #     else:
    #         start, end, sub_exp = sub_expression(exp, i)
    #         operands_lst.append(sub_exp)
    #         i = end
    #
    # if len(operators_lst) == 0:
    #     return float(exp)
    #
    # for i in range(len(operands_lst)):
    #     try:
    #         float(operands_lst[i])
    #     except:
    #         operands_lst[i] = calculate(operands_lst[i])
    #
    # priority = 6
    # while priority > 0:
    #     updated_operators_lst = []
    #     updated_operands_lst = []
    #     operands_index = 0
    #     operators_index = 0
    #     calculated = False
    #     finished_priority = True
    #     while operators_index < len(operators_lst):
    #         if operators_lst[operators_index].get_priority() == priority and not calculated:
    #             calculated = True
    #             op_func = getattr(operators, operators.operators_signs[operators_lst[operators_index].get_sign()])
    #             if "middle" in operators_lst[operators_index].get_places():  # operators_lst[i].get_place() == "middle"
    #                 updated_operands_lst.append(op_func(operands_lst[operands_index], operands_lst[operands_index+1]))
    #                 operands_index += 2
    #             else:  # todo replace with constants
    #                 updated_operands_lst.append(op_func(operands_lst[operands_index]))
    #                 operands_index += 1
    #
    #             operators_index += 1
    #         else:
    #             if calculated:
    #                 finished_priority = False
    #             updated_operands_lst.append(operands_lst[operands_index])
    #             updated_operators_lst.append(operators_lst[operators_index])
    #             operands_index += 1
    #             operators_index += 1
    #     if len(updated_operands_lst) == len(updated_operators_lst) and \
    #             ["left"] != updated_operators_lst[-1].get_places():
    #         updated_operands_lst.append(operands_lst[-1])
    #     if len(updated_operands_lst) > 0:
    #         operators_lst = updated_operators_lst[:]
    #         operands_lst = updated_operands_lst[:]
    #     if finished_priority:
    #         priority -= 1

    # return operands_lst[0]

