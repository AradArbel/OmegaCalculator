"""
Auther: Arad Arbel
Description: this module contains the all the operators calculation functions .
"""
from exceptions import DivisionByZero, ModuloByZero, NegativeFactorial, FloatFactorial, ComplexNumberError, \
    PowerByZeroUndefined, OverMaxValue


def addition(operand1: float, operand2: float) -> float:
    """
    the function calculate addition equation.
    :param: two operands
    :return: the result of the equation.
    """
    return float(operand1) + float(operand2)


def subtraction(operand1: float, operand2: float) -> float:
    """
    the function calculate subtraction equation.
    :param: two operands
    :return: the result of the equation.
    """
    return float(operand1) - float(operand2)


def multiplication(operand1: float, operand2: float) -> float:
    """
    the function calculate multiplication equation.
    :param: two operands
    :return: the result of the equation.
    """
    return float(operand1) * float(operand2)


def division(operand1: float, operand2: float) -> float:
    """
    the function calculate division equation.
    :param: two operands
    :return: the result of the equation.
    """
    # division by zero check
    if float(operand2) == 0:
        raise DivisionByZero
    return float(operand1) / float(operand2)


def power(base: float, exponent: float) -> float:
    """
    the function calculate power equation.
    :param: base and exponent
    :return: the result of the equation.
    """
    # zero power zero check
    if float(base) == 0 and float(exponent) == 0:
        raise PowerByZeroUndefined

    solution = pow(float(base), float(exponent))
    # complex check
    if type(solution) is complex:
        raise ComplexNumberError
    # over max value check
    if solution == float("inf"):
        raise OverMaxValue
    return solution


def modulo(operand1: float, operand2: float) -> float:
    """
    the function calculate modulo equation.
    :param: two operands
    :return: the result of the equation.
    """
    # modulo by zero check
    if float(operand2) == 0:
        raise ModuloByZero
    return float(operand1) % float(operand2)


def maximum(operand1: float, operand2: float) -> float:
    """
    the function calculate maximum number from two numbers.
    :param: two operands
    :return: the result of the equation.
    """

    return float(operand1) if float(operand1) >= float(operand2)else float(operand2)


def minimum(operand1: float, operand2: float) -> float:
    """
    the function calculate minimum number from two numbers.
    :param: two operands
    :return: the result of the equation.
    """
    return float(operand1) if float(operand1) <= float(operand2) else float(operand2)


def average(operand1: float, operand2: float) -> float:
    """
    the function calculate average of two numbers.
    :param: two operands
    :return: the result of the equation.
    """

    return (float(operand1) + float(operand2)) / 2


def negative(operand: float) -> float:
    """
    the function calculate negative number of a number.
    :param: one operand
    :return: the result of the equation.
    """
    return float(operand) * -1


def factorial(operand: float) -> float:
    """
    the function calculate factorial of a number.
    :param: one operand
    :return: the result of the equation.
    """
    # negative factorial check
    if float(operand) < 0:
        raise NegativeFactorial
    # float factorial check
    if int(float(operand)) != float(operand):
        raise FloatFactorial
    if operand == 0:
        return 1
    solution = float(operand) * factorial(float(operand)-1)
    # over max value check
    if solution == float("inf"):
        raise OverMaxValue
    return solution


def sum_digit(operand: any) -> float:
    """
    the function calculate the digit sum of a number.
    :param: one operand
    :return: the result of the equation.
    """
    operand = str(operand)
    digit_sum = 0
    sign = 1
    if operand[0] == '-':
        sign = -1
    for i in range(len(operand)):
        if operand[i] not in ".-":
            digit_sum += float(operand[i])
    return sign * digit_sum
