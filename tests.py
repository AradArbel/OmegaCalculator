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
    simple_equations = {'1.5+2': 'result: 3.5', '5*7': 'result: 35.0', '1-5': 'result: -4.0', '21/7': 'result: 3.0',
                        '10^2': 'result: 100.0', '5%3': 'result: 2.0', '4 $  2': 'result: 4.0', '3!!': 'result: 720.0',
                        '2 & 3': 'result: 2.0', '2 @ 3': 'result: 2.5', '~5': 'result: -5.0', '5!': 'result: 120.0',
                        '123#': 'result: 6.0'}
    for equation, solution in simple_equations.items():
        assert solution == result(equation)


def test_complicated_equations():
    """
    This function tests complicated equations.
    :return: None.
    """
    complicated_equations = {'(17%(3!*4)+2)^(~---2! + 2^3 - (4^2)/2)': 'result: 361.0',
                             '(5!@4%32^2/90*1.5-5+10)*3 + (5-( 2 ^ 32 % 4 @ 5!)#)': 'result: 7.0',
                             '-((6$4*3)*2^-2+(25%(3*596)))+(20-(2^2)@(2*3)-2)': 'result: -16.5',
                             '-((17$4*3)*2^2+(77%(7*7)))*~5-(77@57)': 'result: 1093.0',
                             '(~-----(321312*32)%2^31)*76 -- (5---321 +(21)!)': 'result: 5.109094217170944e+19',
                             '(~-3!+ 2)@4-(75.435%5) #': 'result: -11.0', '3+~5&(90-6)@43.546$4434': 'result: 4437.0',
                             '3!! @(50^2) - (15*7/-(6+9) & (69.96*4))': 'result: 1617.0',
                             '0.8^0.8-0.8--0.8-~0.8-100.919#-~0.001*10^3': 'result: -17.363488357926983',
                             '6$(3*-234#^3 / 12.72@3.5)-100%(13*2.5)': 'result: 3.5',
                             '((5!*~-3)$777)/3.8-((5@3)&(6$3))': 'result: 200.47368421052633',
                             '67.76#*-42&32.32/--3@~7^2-(3!^0.5)---3': 'result: -278.44948974278316',
                             '~-39 ^ 2.5 - 0.013#@0.14# + 8!* -5%3 + 5%-3': 'result: 49813.141955563966'}
    for equation, solution in complicated_equations.items():
        assert solution == result(equation)
