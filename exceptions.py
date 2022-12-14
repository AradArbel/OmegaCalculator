"""
Auther: Arad Arbel
Description: this module contains all the exceptions that might come by using the calculator.
"""


class CalculatorException(Exception):
    def __init__(self, message):
        super().__init__(message)


class UnBalancedParenthesis(CalculatorException):
    def __init__(self):
        super().__init__("Error: unbalanced parentheses")


class NegativeFactorial(CalculatorException):
    def __init__(self):
        super().__init__("Error: negative factorial undefined")


class FloatFactorial(CalculatorException):
    def __init__(self):
        super().__init__("Error: non integer factorial undefined")


class UnsupportedChar(CalculatorException):
    def __init__(self, c):
        super().__init__(f"Error: unsupported character: {c}")


class InsufficientArguments(CalculatorException):
    def __init__(self, places, op_sign):
        if places == ["left"]:
            super().__init__(f"Error: {op_sign} must have argument to the right")
        elif places == ["right"]:
            super().__init__(f"Error: {op_sign} must have argument to the left")
        elif places == ["middle"]:
            super().__init__(f"Error: {op_sign} must have argument to the left and right")
        else:
            super().__init__(f"Error: {op_sign} must have argument to the left or to the left and right")


class ConsecutiveArguments(CalculatorException):
    def __init__(self):
        super().__init__("Error: consecutive arguments")


class DivisionByZero(CalculatorException):
    def __init__(self):
        super().__init__("Error: division by zero")


class ModuloByZero(CalculatorException):
    def __init__(self):
        super().__init__("Error: modulo by zero")


class TooManyDecimalPoints(CalculatorException):
    def __init__(self):
        super().__init__("Error: too many decimal points")


class EmptyInput(CalculatorException):
    def __init__(self):
        super().__init__("Error: empty input")
