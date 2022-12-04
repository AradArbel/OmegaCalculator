import operators
import operatorx


class Calculate:

    def calculate(self, exp: str) -> float:
        start_index = 0  # 3 + 4 * 5
        balance = 0
        operands_lst = []  # [3,4,5]
        operators_lst = []  # ['+', '*']
        for i in range(len(exp)):
            # if exp[i] == ")":
            #     operands_lst.append(exp[start_index+1:i])
            #     start_index = i
            if exp[i] in operators.operators_signs.keys() and balance == 0:
                operators_lst.append(operatorx.OperatorX(exp[i], i))
            else:
                operands_lst.append(exp[i])
                start_index = i
        if len(operators_lst) == 0:
            return float(exp)
        if len(operators_lst) == 1:
            op_func = getattr(operators, operators.operators_signs[operators_lst[0].get_sign()])
            if operators_lst[0].get_place() == "left":  # todo replace with enum instead of str
                right = self.calculate(exp[operators_lst[0].get_index() + 1:])
                return op_func(right)
            elif operators_lst[0].get_place() == "middle":
                left = self.calculate(exp[:operators_lst[0].get_index()])
                right = self.calculate(exp[operators_lst[0].get_index() + 1:])
                return op_func(left, right)
            else:
                left = self.calculate(exp[:operators_lst[0].get_index()])
                return op_func(left)
        for priority in range(operatorx.MAX_PRIORITY, 0, -1):
            for op_sign in operators_lst:
                if op_sign.get_priority() == priority:
                    op_func = getattr(operators, operators.operators_signs[op_sign.get_sign()])
                    if op_sign.get_place() == "left":  # todo replace with enum instead of str
                        right = self.calculate(exp[op_sign.get_index() + 1:])
                        return op_func(right)
                    elif op_sign.get_place() == "middle":
                        left = self.calculate(exp[:op_sign.get_index()])
                        right = self.calculate(exp[op_sign.get_index() + 1:])
                        return op_func(left, right)
                    else:
                        left = self.calculate(exp[:op_sign.get_index()])
                        return op_func(left)


c = Calculate()
print(c.calculate("5+6*8"))
