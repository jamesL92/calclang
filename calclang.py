from lexer import Lexer
from interpreter import Interpreter
from calclang_parser import Parser

class Calclang:
    def __init__(self):
        self.lexer = Lexer()
        self.parser = Parser()
        self.interpreter = Interpreter()

    def run_statement(self, statement):
        tokens = self.lexer.tokenise(statement)
        ast = self.parser.parse(tokens)
        result = self.interpreter.interpret(ast)
        return result
