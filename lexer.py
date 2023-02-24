from tokens import Token, TokenType
from typing import List

class Lexer():
    def tokenise(self, statement: str) -> list[Token]:
        self.characters = [char for char in statement]
        self.current_index = 0
        self.current_character = self.characters[self.current_index]
        tokens = []
        while self.current_character != None:
            if self.current_character in ' \n\t':
                self.advance()
            elif self.current_character.isnumeric():
                tokens.append(self.build_number())
            elif self.current_character == '+':
                tokens.append(Token(TokenType.ADD))
                self.advance()
            elif self.current_character == '-':
                tokens.append(Token(TokenType.SUBTRACT))
                self.advance()
            elif self.current_character == '*':
                tokens.append(Token(TokenType.MULTIPLY))
                self.advance()
            elif self.current_character == '/':
                tokens.append(Token(TokenType.DIVIDE))
                self.advance()
            elif self.current_character == '^':
                tokens.append(Token(TokenType.EXPONENTIAL))
                self.advance()
            elif self.current_character == '(':
                tokens.append(Token(TokenType.LBRACKET))
                self.advance()
            elif self.current_character == ')':
                tokens.append(Token(TokenType.RBRACKET))
                self.advance()
            elif self.current_character in 'sct':
                tokens.append(self.build_trig())
            else:
                raise Exception(f'Unknown character {self.current_character}')

        return tokens

    def advance(self):
        self.current_index += 1
        if self.current_index >= len(self.characters):
            self.current_character = None
            return
        self.current_character = self.characters[self.current_index]

    def build_number(self) -> Token:
        number_string = self.current_character
        dot_count = 0
        self.advance()
        while self.current_character is not None and (self.current_character.isnumeric() or self.current_character == '.'):
            if self.current_character == '.':
                dot_count += 1
                if dot_count > 1:
                    raise Exception("Multiple dots")
            number_string += self.current_character
            self.advance()
        return Token(TokenType.NUMBER, float(number_string))

    def build_trig(self) -> Token:
        trig_string = self.current_character
        for _ in range(2):
            self.advance()
            if self.current_character == None:
                raise Exception(f'Unknown character {self.current_character}')
            trig_string += self.current_character
        if trig_string not in ['sin', 'cos', 'tan']:
            raise Exception(f'Invalid trig function')
        self.advance()
        return Token(TokenType.TRIG, trig_string)