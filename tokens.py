from enum import Enum
from typing import Any, Optional

class TokenType(Enum):
    NUMBER = "NUMBER"
    ADD = "ADD"
    SUBTRACT = "SUBTRACT"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"
    EXPONENTIAL = "EXPONENTIAL"
    LBRACKET = "LBRACKET"
    RBRACKET = "RBRACKET"
    TRIG = "TRIG"

class Token:
    def __init__(self, token_type: TokenType, value: Optional[Any] = None) -> None:
        self.token_type = token_type
        self.value = value
