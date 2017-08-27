from memory import *
from input import *
from output import *
from source import *



class BrainfuckInterpreter:

    def __init__(self, source, input, output):
        self.token_interpreters = {
            '>': self._moveRight,
            '<': self._moveLeft,
            '+': self._increase,
            '-': self._decrease,
            ',': self._in,
            '.': self._out,
            '[': self._startLoop,
            ']': self._endLoop
        }

    def _moveRight(self):
        pass
    def _moveLeft(self):
        pass
    def _increase(self):
        pass
    def _decrease(self):
        pass
    def _in(self):
        pass
    def _out(self, value):
        pass
    def _startLoop(self):
        pass
    def _endLoop(self):
        pass

    def run(self):
        pass





BrainfuckInterpreter(FileSource('helloworld.b'), StdinInput(), StdinOutput()).run()

