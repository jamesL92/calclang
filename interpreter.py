import nodes
import math

class Interpreter():
    def interpret(self, ast: nodes.BaseNode):
        return self.evaluate(ast)

    def evaluate(self, node: nodes.BaseNode):
        node_name = type(node).__name__
        return getattr(self, f'evaluate_{node_name}', self.evaluate_default)(node)

    def evaluate_NumberNode(self, node: nodes.NumberNode):
        return node.number

    def evaluate_AdditionNode(self, node: nodes.AdditionNode):
        return self.evaluate(node.left_node) + self.evaluate(node.right_node)

    def evaluate_SubtractionNode(self, node: nodes.SubtractionNode):
        return self.evaluate(node.left_node) - self.evaluate(node.right_node)

    def evaluate_MultiplicationNode(self, node: nodes.MultiplicationNode):
        return self.evaluate(node.left_node) * self.evaluate(node.right_node)

    def evaluate_DivisionNode(self, node: nodes.DivisionNode):
        return self.evaluate(node.left_node) / self.evaluate(node.right_node)

    def evaluate_TrigNode(self, node: nodes.TrigNode):
        if node.trig_function == 'sin':
            return math.sin(self.evaluate(node.node))
        if node.trig_function == 'cos':
            return math.cos(self.evaluate(node.node))
        if node.trig_function == 'tan':
            return math.tan(self.evaluate(node.node))
        raise Exception('Invalid trig identity')

    def evaluate_default(self, node: nodes.BaseNode):
        raise Exception(f'Unknown node of type {type(node).__name__}')