from .tokens import Token, TokenType
from .lexer import Lexer


class InterpreterException(Exception):
    ...


class Interpreter:

    def __init__(self):
        self.current_token: Token = None
        self.lexer = Lexer()

    def check_type(self, type_: TokenType):
        if self.current_token.type == type_:
            self.current_token = self.lexer.next()
            return
        raise InterpreterException(
            f"Invalid token order. Expected {type_}, Received {self.current_token}")

    def factor(self) -> float:
        token = self.current_token
        self.check_type(TokenType.NUMBER)
        return float(token.value)

    def term(self) -> float:
        ops = [TokenType.DIV, TokenType.MUL]
        result = self.factor()
        while self.current_token.type in ops:
            token = self.current_token
            match token.type:
                case TokenType.DIV:
                    self.check_type(TokenType.DIV)
                    result /= self.factor()
                case TokenType.MUL:
                    self.check_type(TokenType.MUL)
                    result *= self.factor()
        return result

    def expr(self) -> float:
        ops = [TokenType.PLUS, TokenType.MINUS]
        result = self.term()
        while self.current_token.type in ops:
            token = self.current_token
            match token.type:
                case TokenType.PLUS:
                    self.check_type(TokenType.PLUS)
                    result += self.term()
                case TokenType.MINUS:
                    self.check_type(TokenType.MINUS)
                    result -= self.term()
        return result

    def eval(self, s: str) -> float:
        self.lexer.init_lexer(s)
        self.current_token = self.lexer.next()
        return self.expr()