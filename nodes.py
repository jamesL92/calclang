class BaseNode:
    pass

class NumberNode(BaseNode):
    def __init__(self, number: float):
        self.number = number

class AdditionNode(BaseNode):
    def __init__(self, left_node: BaseNode, right_node: BaseNode):
        self.left_node = left_node
        self.right_node = right_node

class SubtractionNode(BaseNode):
    def __init__(self, left_node: BaseNode, right_node: BaseNode):
        self.left_node = left_node
        self.right_node = right_node

class MultiplicationNode(BaseNode):
    def __init__(self, left_node: BaseNode, right_node: BaseNode):
        self.left_node = left_node
        self.right_node = right_node

class DivisionNode(BaseNode):
    def __init__(self, left_node: BaseNode, right_node: BaseNode):
        self.left_node = left_node
        self.right_node = right_node

class ExponentialNode(BaseNode):
    def __init__(self, base_node: BaseNode, power_node: BaseNode):
        self.base_node = base_node
        self.power_node = power_node

class TrigNode(BaseNode):
    def __init__(self, trig_function: str, node: BaseNode):
        self.trig_function = trig_function
        self.node = node