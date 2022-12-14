from exceptions import DivisionByZero, ModuloByZero, NegativeFactorial, FloatFactorial

"""
Auther: Arad Arbel
Description: this module contains the all the operators calculation functions .
"""


def addition(operand1: float, operand2: float) -> float:
    return float(operand1) + float(operand2)


def subtraction(operand1: float, operand2: float) -> float:
    return float(operand1) - float(operand2)


def multiplication(operand1: float, operand2: float) -> float:
    return float(operand1) * float(operand2)


def division(operand1: float, operand2: float) -> float:
    if float(operand2) == 0:
        raise DivisionByZero
    return float(operand1) / float(operand2)


def power(base: float, exponent: float) -> float:
    return pow(float(base), float(exponent))


def modulo(operand1: float, operand2: float) -> float:
    if float(operand2) == 0:
        raise ModuloByZero
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
    if float(operand1) < 0:
        raise NegativeFactorial
    if int(float(operand1)) != float(operand1):
        raise FloatFactorial
    fact = 1
    for i in range(1, int(operand1) + 1):
        fact = fact * i
    return float(fact)


def sum_digit(operand1: any) -> float:
    operand1 = str(operand1)
    digit_sum = 0
    sign = 1
    if operand1[0] == '-':
        sign = -1
    # Single line that calculates sum of digits
    for i in range(len(operand1)):
        if operand1[i] not in ".-":
            digit_sum += float(operand1[i])
    return sign * digit_sum
