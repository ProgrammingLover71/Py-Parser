from enum import Enum

"""
Utility class for representing types of tokens.
It provides a simple way for keeping information about tokens in the source code.
"""
class TokenType:
    def __init__(self, name: str, contains_syntax: bool = False):
        self.name = name
        self.contains_syntax = contains_syntax
    
    def __repr__(self):
        return f'TokenType({self.name})'
    

class TokenTypes(Enum):
    EOF = TokenType('EOF')
    NUMBER = TokenType('NUMBER', True)


"""
The `Token` class provides a way of representing the source code in an easy to parse way.
"""
class Token:
    def __init__(self, tok_type: TokenType, line: int, col: int, tok_value=None):
        self.type = tok_type
        self.value = tok_value if tok_type.contains_syntax else None
        self.line = line
        self.column = col
    
    def __repr__(self):
        return f'Token(type={self.type}, value="{self.value}", pos={self.line}:{self.column})'