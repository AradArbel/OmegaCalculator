"""
Auther: Arad Arbel
Description: this module contains the operator class and operators dictionaries by there priority, place and name.
"""

OPERATORS_PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3,
                      '%': 4, '$': 5, '&': 5, '@': 6, '~': 6, '!': 6,
                      '#': 6}

OPERATORS_PLACE = {'+': ['middle'], '-': ['middle', 'left'], '*': ['middle'], '/': ['middle'], '^': ['middle'],
                   '%': ['middle'], '$': ['middle'], '&': ['middle'], '@': ['middle'], '~': ['left'], '!': ['right'],
                   '#': ['right']}

OPERATORS_NAME = {'+': 'addition', '-': 'subtraction', '*': 'multiplication', '/': 'division', '^': 'power',
                  '%': 'modulo', '$': 'maximum', '&': 'minimum', '@': 'average', '~': 'negative', '!': 'factorial',
                  '#': 'sum_digit'}


class Operator:
    def __init__(self, sign):
        self.__sign = sign
        self.__priority = OPERATORS_PRIORITY[sign]
        self.__places = OPERATORS_PLACE[sign]

    def __repr__(self):
        return self.__sign

    def get_priority(self):
        return self.__priority

    def get_places(self):
        return self.__places

    def get_sign(self):
        return self.__sign
