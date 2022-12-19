"""
Auther: Arad Arbel
Description: this module contains the welcome message to the user and the options to add equation and exit.
"""

from calculate import calculate
from exceptions import CalculatorException
from validation import validate

WELCOME_MESSAGE = "Welcome to the Omega Calculator." \
                  "This calculator is very unique and has a lot of special operators like:" \
                  " $ - maximum, & - minimum,@ - average, ~ - negative, # - digit sum "\
                  "and of course also all the other simple operators"

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
        print("End of file error")
        print(EXIT_MESSAGE)
        exit(1)
    except KeyboardInterrupt:
        print("Key board interrupt error")
        print(EXIT_MESSAGE)
        exit(1)
    except OSError:
        print("File descriptor is not associated with any terminal device")
        exit(1)


def result(equation):
    """
        the function calculate the equation or raise exception if something went wrong.
        :return: the result of the equation or exception.
    """
    try:
        validate(equation)
        return f"result: {calculate(equation)}"
    except CalculatorException as exception:
        return exception
    except OverflowError as OFE:
        return OFE
    except RecursionError as RE:
        return RE


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
