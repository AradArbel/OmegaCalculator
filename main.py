from calculate import calculate
from validation import validate


def main():
    exp = "(1-1)+(1--1)+(1---1)"
    # validate(exp)
    print(calculate(exp))

    try:
        exp = "1-3^2"
        validate(exp)
        print(calculate(exp))
    except Exception as e:
        print(e)

    # while True:
    #     exp = input("Please enter expression:")
    #     try:
    #         validate(exp)
    #         print(Calculate.calculate(exp))
    #         action = input("x - for exit or anything else to continue")
    #     except Exception as e:
    #         print(e)

main()