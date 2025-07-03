class TokenType:
    def __init__(self, name: str, contains_syntax: bool = False):
        self.name = name
        self.contains_syntax = contains_syntax
    
    def __repr__(self):
        return f'TokenType({self.name})'
    
    def __call__(self, value):
        pass