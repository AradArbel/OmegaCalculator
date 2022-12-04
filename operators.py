# operators_signs = {'Addition': '+', 'subtraction': '-', 'Multiplication': '*', 'Division': '/', 'Power': '^',
#                    'Modulo': '%', 'Maximum': '$', 'Minimum': '&', 'Average': '@', 'Negative': '~', 'Factorial': '!',
#                    'Sum_digit': '#'}
operators_signs = {'+': 'addition', '-': 'subtraction', '*': 'multiplication', '/': 'division', '^': 'power',
                   '%': 'modulo', '$': 'maximum', '&': 'minimum', '@': 'average', '~': 'negative', '!': 'factorial',
                   '#': 'sum_digit'}


def addition(operand1: float, operand2: float) -> float:
    return float(operand1) + float(operand2)


def subtraction(operand1: float, operand2: float) -> float:
    return float(operand1) - float(operand2)


def multiplication(operand1: float, operand2: float) -> float:
    return float(operand1) * float(operand2)


def division(operand1: float, operand2: float) -> float:
    return float(operand1) / float(operand2)


def power(base: float, exponent: float) -> float:
    return float(pow(base, exponent))


def modulo(operand1: float, operand2: float) -> float:
    return float(operand1) % float(operand2)


def maximum(operand1: float, operand2: float) -> float:
    return float(operand1) if operand1 >= operand2 else float(operand2)


def minimum(operand1: float, operand2: float) -> float:
    return float(operand1) if operand1 <= operand2 else float(operand2)


def average(operand1: float, operand2: float) -> float:
    return (float(operand1) + float(operand2)) / 2


def negative(operand1: float) -> float:
    return float(operand1) * -1


def factorial(operand1: float) -> float:
    fact = 1
    for i in range(1, int(operand1) + 1):
        fact = fact * i
    return float(fact)


def sum_digit(operand1: float) -> float:
    digit_sum = 0
    # Single line that calculates sum of digits
    while operand1 > 0:
        digit_sum += int(operand1 % 10)
        operand1 = int(operand1 / 10)
    return digit_sum
