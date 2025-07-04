from token import *

class Lexer:
    def __init__(self):
        self.reset()
    
    """Reset the lexer to a blank state."""
    def reset(self):
        self.source = ""
        self.line = 1
        self.column = -1
        self._index = -1   # Used internally
        self.current = chr(0)   # The null character
        self.advance()
    
    """Advance the lexer to the next character in the source code."""
    def advance(self):
        is_newline = (self.current == '\n')
        # Update the line and column for creating tokens
        if is_newline:
            self.line += 1
            self.column = 1
        else:
            self.column += 1
        # Update the lexer's internal position in the source
        self._index += 1
        if self._index < len(self.source):
           self.current = self.source[self._index]
        else:
            self.current = chr(0)
            