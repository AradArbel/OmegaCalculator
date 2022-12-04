import operators

MAX_PRIORITY = 6


class OperatorX:

    def __init__(self, sign, index):
        self.__priority = 6
        self.__sign = sign
        self.__place = "middle"
        self.__index = index
        # todo add enum

    def get_priority(self):
        return self.__priority

    def get_place(self):
        return self.__place  # todo add code

    def get_index(self):
        return self.__index

    def get_sign(self):
        return self.__sign
