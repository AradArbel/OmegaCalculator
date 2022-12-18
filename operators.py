from exceptions import DivisionByZero, ModuloByZero, NegativeFactorial, FloatFactorial, ComplexNumberError, \
    PowerByZeroUndefined

"""
Auther: Arad Arbel
Description: this module contains the all the operators calculation functions .
"""


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
    if base == 0 and exponent == 0:
        raise PowerByZeroUndefined

    solution = pow(float(base), float(exponent))
    # complex check
    if type(solution) is complex:
        raise ComplexNumberError
    else:
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

    return float(operand1) if operand1 >= operand2 else float(operand2)


def minimum(operand1: float, operand2: float) -> float:
    """
    the function calculate minimum number from two numbers.
    :param: two operands
    :return: the result of the equation.
    """
    return float(operand1) if operand1 <= operand2 else float(operand2)


def average(operand1: float, operand2: float) -> float:
    """
    the function calculate average of two numbers.
    :param: two operands
    :return: the result of the equation.
    """

    return (float(operand1) + float(operand2)) / 2


def negative(operand1: float) -> float:
    """
    the function calculate negative number of a number.
    :param: one operand
    :return: the result of the equation.
    """
    return float(operand1) * -1


def factorial(operand1: float) -> float:
    """
    the function calculate factorial of a number.
    :param: one operand
    :return: the result of the equation.
    """
    # negative factorial check
    if float(operand1) < 0:
        raise NegativeFactorial
    # float factorial check
    if int(float(operand1)) != float(operand1):
        raise FloatFactorial
    fact = 1
    for i in range(1, int(operand1) + 1):
        fact = fact * i
    return float(fact)


def sum_digit(operand1: any) -> float:
    """
    the function calculate the digit sum of a number.
    :param: one operand
    :return: the result of the equation.
    """
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
