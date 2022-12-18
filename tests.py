"""
Auther: Arad Arbel
Description: this module contains the pytest testing for the calculator.
"""

import pytest

import exceptions
from exceptions import CalculatorException, DivisionByZero, UnsupportedChar
from user import result


def test_syntax_error():
    """
    This function tests syntax errors.
    :return: None.
    """
    test = ["5*9a+4", "5*9+2.22.5+2.1", "(((1+5))(", "5**9", "10-+5"]
    for equation in test:
        solution = result(equation)
        assert isinstance(solution, CalculatorException)


def test_nonsense():
    """
    This function tests syntax errors.
    :return: None.
    """
    test = "ghsdfljikghSDLJre345857489+*(^#^@"
    solution = result(test)
    assert type(solution) is UnsupportedChar


def test_white_space():
    """
    This function tests space white.
    :return: None.
    """
    test = [" \t", " ", "\n", "\t  \n\n"]
    for equation in test:
        solution = result(equation)
        assert isinstance(solution, CalculatorException)


def test_basic_equations():
    """
    This function tests basic equations.
    :return: None.
    """
    simple_equations = {'1+2': 'result: 3.0', '5*7': 'result: 35.0', '1-5': 'result: -4.0', '21/7': 'result: 3.0',
                        '10^2': 'result: 100.0', '5%3': 'result: 2.0', '4 $  2': 'result: 4.0', '3!!': 'result: 720.0',
                        '2 & 3': 'result: 2.0', '2 @ 3': 'result: 2.5', '~5': 'result: -5.0', '5!': 'result: 120.0',
                        '123#': 'result: 6.0'}
    for equation, solution in simple_equations.items():
        assert solution == result(equation)
