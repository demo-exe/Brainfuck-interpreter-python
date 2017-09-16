from .log import logger

class Interpreter:

    def __init__(self, source, input, output, memory):
        logger.debug("Constructing interpreter")
        self.source = source
        self.input = input
        self.output = output
        self.memory = memory

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
        self.memory.MoveRight()
        self.IP += 1
    def _moveLeft(self):
        self.memory.MoveLeft()
        self.IP += 1
    def _increase(self):
        self.memory.Increase()
        self.IP += 1
    def _decrease(self):
        self.memory.Decrease()
        self.IP += 1
    def _in(self):
        self.memory.SetCell(self.input.getNext())
        self.IP += 1
    def _out(self):
        self.output.putNext(self.memory.GetCell())
        self.IP += 1

    def _startLoop(self):
        stack = 0
        tmpIP = self.IP + 1
        if self.memory.GetCell() == 0:
            while True:
                token = self.source.getToken(tmpIP)
                if token == ']': #find matching closing bracket
                    if stack == 0: #stack is empty - this is a matching bracket
                        logger.info("Ending loop: jumping from %i to %i" % (self.IP, tmpIP + 1))
                        self.IP = tmpIP + 1 # jump to instruction after it
                        break
                    else:
                        stack -= 1 #nested loop ended
                elif token == '[': #found nested loop - increase stack
                    stack += 1
                tmpIP += 1
        else: #cell != 0 proceed to next instruction
            self.IP += 1
            logger.info("Cell=%i continuing to code inside loop" % (self.memory.GetCell()))

    def _endLoop(self):
        stack = 0
        tmpIP = self.IP - 1 #this time we do reverse search

        while True:
            token = self.source.getToken(tmpIP)
            if token == '[': #find matching opening bracket
                if stack == 0: #stack is empty - this is matching bracket
                    self.IP = tmpIP # jump to it
                    logger.info("Jumping to opening bracket on: %i" % (tmpIP))
                    break
                else:
                    stack -= 1 #nested loop ended
            elif token == ']': #found nested loop - increase stack
                stack += 1
            tmpIP -= 1


    def run(self):
        logger.debug("Beginning run() IP=%i" % self.IP)
        nexti = self.source.getToken(self.IP)
        while nexti != 0:
            logger.info("Next instruction : '%s' IP=%i" % (nexti, self.IP))
            self.token_interpreters[nexti]()
            nexti = self.source.getToken(self.IP)
        
        logger.info("Reached program end. IP=%i" % self.IP)

