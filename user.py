"""
Auther: Arad Arbel
Description: this module contains the welcome message to the user and the options to add equation and exit.
"""
from typing import Union

from calculate import calculate
from exceptions import CalculatorException
from validation import validate

WELCOME_MESSAGE = "Welcome to the Omega Calculater." \
                  "This calculater is very unique and has a lot of special operators like:" \
                  " $ - maximum, & - minimum,@ - average, ~ - negative, # - digit sum" \
                  "Have fun solving equations. "
EXIT_MESSAGE = "Bye bye"


def get_input() -> str:
    """
        the function gets the equation to solve from the user.
        :return: the equation in string type.
    """
    try:
        equation = input("Please enter the equation you want to calculate or press E to exit:\n")
        return equation
    except EOFError:
        print("end of file error")
        print(EXIT_MESSAGE)
        exit(1)


def result(equation) -> Union[str, CalculatorException]:
    """
        the function calculate the equation or raise exception if somthing went wrong.
        :return: the result of the equation.
    """
    try:
        validate(equation)
        return f"result: {calculate(equation)}"
    except CalculatorException as exception:
        return exception


def interface() -> None:
    """
    the function handling the user interface.
    :return: None
    """
    print(WELCOME_MESSAGE)
    while True:
        equation = get_input()
        if equation.lower() == "e":
            print(EXIT_MESSAGE)
            break
        else:
            print(result(equation))
            print("You can enter another equation or exit \n")
