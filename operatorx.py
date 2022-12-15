import operators

# MAX_PRIORITY = 6

OPERATORS_PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3,
                      '%': 4, '$': 5, '&': 5, '@': 6, '~': 6, '!': 6,
                      '#': 6}
OPERATORS_PLACE = {'+': 'middle', '-': 'middle', '*': 'middle', '/': 'middle', '^': 'middle',
                   '%': 'middle', '$': 'middle', '&': 'middle', '@': 'middle', '~': 'left', '!': 'right',
                   '#': 'right'}


class OperatorX:

    def __init__(self, sign):
        self.__sign = sign
        self.__priority = OPERATORS_PRIORITY[sign]
        self.__place = OPERATORS_PLACE[sign]

    def get_priority(self):
        return self.__priority

    def get_place(self):
        return self.__place

    def get_sign(self):
        return self.__sign