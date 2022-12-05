import operators
import operatorx


class Calculate:

    # todo clean spaces, support more than one digit, validation, exceptions
    # (...) operator (...) / (...) operator / operator (...) / ....
    def sub_expression(self, exp: str, start: int):
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

    def calculate(self, exp: str) -> float:
        balance = 0
        operands_lst = []  # [3,4,5]
        operators_lst = []  # ['+', '*']
        i = 0
        while i < len(exp):
            if exp[i] in operators.operators_signs.keys() and balance == 0:
                operators_lst.append(operatorx.OperatorX(exp[i]))
                i += 1
            else:
                start, end, sub_exp = self.sub_expression(exp, i)
                operands_lst.append(sub_exp)
                i = end

        if len(operators_lst) == 0:
            return float(exp)

        for i in range(len(operands_lst)):
            try:
                float(operands_lst[i])
            except:
                operands_lst[i] = self.calculate(operands_lst[i])


        priority = 6
        while priority > 0:
            updated_operators_lst = []
            updated_operands_lst = []
            operands_index = 0
            operators_index = 0
            calculated = False
            finished_priority = True
            while operators_index < len(operators_lst):
                if operators_lst[operators_index].get_priority() == priority and not calculated:
                    calculated = True
                    op_func = getattr(operators, operators.operators_signs[operators_lst[operators_index].get_sign()])
                    if operators_lst[operators_index].get_place() == "left" or operators_lst[operators_index].get_place() == "right":  # todo replace with constants
                        updated_operands_lst.append(op_func(operands_lst[operands_index]))
                        operands_index += 1
                    else:  # operators_lst[i].get_place() == "middle"
                        updated_operands_lst.append(op_func(operands_lst[operands_index], operands_lst[operands_index+1]))
                        operands_index += 2
                    operators_index += 1
                else:
                    if calculated:
                        finished_priority = False
                    updated_operands_lst.append(operands_lst[operands_index])
                    updated_operators_lst.append(operators_lst[operators_index])
                    operands_index += 1
                    operators_index += 1
            if len(updated_operands_lst) > 0:
                operators_lst = updated_operators_lst[:]
                operands_lst = updated_operands_lst[:]
            if finished_priority:
                priority -= 1

        return operands_lst[0]

        # while operand_index < len(operators_lst):
        #     op_func = getattr(operators, operators.operators_signs[operators_lst[0].get_sign()])
        #     if operators_lst[0].get_place() == "left":  # todo replace with enum instead of str
        #         operators_lst[operator_index] = self.calculate(operands_lst[operand_index])
        #     elif operators_lst[0].get_place() == "middle":
        #         left = self.calculate(exp[:operators_lst[0].get_index()])
        #         right = self.calculate(exp[operators_lst[0].get_index() + 1:])
        #         return op_func(left, right)
        #     else:
        #         left = self.calculate(exp[:operators_lst[0].get_index()])
        #         return op_func(left)
        # if len(operators_lst) == 1:
        #     op_func = getattr(operators, operators.operators_signs[operators_lst[0].get_sign()])
        #     if operators_lst[0].get_place() == "left":  # todo replace with enum instead of str
        #         right = self.calculate(exp[operators_lst[0].get_index() + 1:])
        #         return op_func(right)
        #     elif operators_lst[0].get_place() == "middle":
        #         left = self.calculate(exp[:operators_lst[0].get_index()])
        #         right = self.calculate(exp[operators_lst[0].get_index() + 1:])
        #         return op_func(left, right)
        #     else:
        #         left = self.calculate(exp[:operators_lst[0].get_index()])
        #         return op_func(left)
        # for priority in range(operatorx.MAX_PRIORITY, 0, -1):
        #     for op_sign in operators_lst:
        #         if op_sign.get_priority() == priority:
        #             op_func = getattr(operators, operators.operators_signs[op_sign.get_sign()])
        #             if op_sign.get_place() == "left":  # todo replace with enum instead of str
        #                 right = self.calculate(exp[op_sign.get_index() + 1:])
        #                 return op_func(right)
        #             elif op_sign.get_place() == "middle":
        #                 left = self.calculate(exp[:op_sign.get_index()])
        #                 right = self.calculate(exp[op_sign.get_index() + 1:])
        #                 return op_func(left, right)
        #             else:
        #                 left = self.calculate(exp[:op_sign.get_index()])
        #                 return op_func(left)


c = Calculate()
print(c.calculate("(15+10)*(40/20+5)")) # "(15+10)*(40/20+5)"
print(c.calculate("6+6+"))
