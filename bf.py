from memory import *
from input import *
from output import *
from source import *



class BrainfuckInterpreter:

    def __init__(self, source, input, output):
        self.source = source
        self.input = input
        self.output = output

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

        #Instruction Pointer
        self.IP = 0

    def _moveRight(self):
        self.IP += 1
    def _moveLeft(self):
        self.IP += 1
    def _increase(self):
        self.IP += 1
    def _decrease(self):
        self.IP += 1
    def _in(self):
        self.IP += 1
    def _out(self):
        self.IP += 1
    def _startLoop(self):
        self.IP += 1
    def _endLoop(self):
        self.IP += 1

    def run(self):
        nexti = self.source.getToken(self.IP)
        while nexti != 0:
            self.token_interpreters[nexti]()
            nexti = self.source.getToken(self.IP)






BrainfuckInterpreter(FileSource('helloworld.b'), StdinInput(), StdinOutput()).run()

