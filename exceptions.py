class UnBalancedParenthesis(Exception):
    def __init__(self):
        super().__init__("Error: unbalanced parentheses")
