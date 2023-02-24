import nodes
from tokens import TokenType, Token

class Parser():
    def parse(self, tokens: list[Token]):
        self.tokens = tokens
        self.current_index = 0
        self.current_token = self.tokens[self.current_index]

        while self.current_token is not None:
            ast = self.expr()

        return ast

    def expr(self):
        if self.current_token.token_type == TokenType.TRIG:
            return self.trig_expr()
        return self.add_expr()

    def trig_expr(self):
        if self.current_token.token_type != TokenType.TRIG:
            raise Exception('Invalid trig string')
        trig_function = self.current_token.value
        self.advance()
        if self.current_token.token_type != TokenType.LBRACKET:
            raise Exception('Expected ( after trig function')
        self.advance()
        node = self.expr()
        if self.current_token.token_type != TokenType.RBRACKET:
            raise Exception('Unclosed parenthesis, expected )')
        self.advance()
        return nodes.TrigNode(trig_function, node)

    def add_expr(self):
        left = self.mult_expr()
        if self.current_token is None:
            return left
        if self.current_token.token_type == TokenType.ADD:
            self.advance()
            right = self.add_expr()
            return nodes.AdditionNode(left, right)
        if self.current_token.token_type == TokenType.SUBTRACT:
            self.advance()
            right = self.add_expr()
            return nodes.SubtractionNode(left, right)
        return left

    def mult_expr(self):
        left = self.exp_expr()
        if self.current_token is None:
            return left
        if self.current_token.token_type == TokenType.MULTIPLY:
            self.advance()
            right = self.mult_expr()
            return nodes.MultiplicationNode(left, right)
        if self.current_token.token_type == TokenType.DIVIDE:
            self.advance()
            right = self.mult_expr()
            return nodes.DivisionNode(left, right)
        return left

    def exp_expr(self):
        left = self.atom()
        if self.current_token is None:
            return left
        if self.current_token.token_type == TokenType.EXPONENTIAL:
            self.advance()
            right = self.exp_expr()
            return nodes.ExponentialNode(left, right)
        return left

    def atom(self):
        node = None
        if self.current_token.token_type == TokenType.NUMBER:
            node = nodes.NumberNode(self.current_token.value)
            self.advance()
        elif self.current_token.token_type == TokenType.LBRACKET:
            self.advance()
            node = self.expr()
            if self.current_token.token_type != TokenType.RBRACKET:
                raise Exception("Unclosed parenthesis, expected )")
            self.advance()
        if node is None:
            raise Exception("Expected number, (, or )")
        return node

    def advance(self):
        self.current_index += 1
        if self.current_index >= len(self.tokens):
            self.current_token = None
            return
        self.current_token = self.tokens[self.current_index]