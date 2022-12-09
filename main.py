from calculate import calculate
from validation import validate
from exceptions import CalculatorException


def main():
    try:
        exp = input("Please enter expression:\n")
        validate(exp)
        print(calculate(exp))
    except EOFError as e:
        print(e)
    except CalculatorException as e:
        print(e)

    # while True:
    #     exp = input("Please enter expression:")
    #     try:
    #         validate(exp)
    #         print(Calculate.calculate(exp))
    #         action = input("x - for exit or anything else to continue")
    #     except Exception as e:
    #         print(e)

# main()

def test():
    try:
        #validate("5*9a+4")
        #validate("5*9+2.22.5+2.1")
        #validate("(((1+5))(")
        #validate("5**9")
        validate("(2+4))(")
        #validate("fdhasfdhsafsda")
        #validate("")
        simple_equations = ['1+2', '5*7', '1-5', '5/7', '10^2', '5%3', '4 $  2', '3 $ 5', '2 & 3', '2 @ 3', '~5', '5!', '123#']
        simple_sols = [3, 35, -4, 5/7, 2, 4, 5, 2, 2.5, -5, 120, 6]
        for i in range(len(simple_sols)):
            assert(calculate(simple_equations[i]) == simple_sols[i])
    except Exception as e:
        print(e)



test()