from .log import logger

class OutOfMemoryException(Exception):
    def __init__(self, mem_index=None):
        if(mem_index == None):
            super().__init__()
        else:
            super().__init__('Error at index : %i' % mem_index)



class Memory:
    def __init__(self, size=30000, 
                       wrap=True, maxint=256):
        logger.info('Constructing memory(size=%i, wrap=%i, maxint=%i)' % (size, wrap, maxint))
        self.mem = [0]
        if(size == -1):
            self.dynamic = True
            self.minpos = 0
            self.maxpos = 0
        else:
            self.dynamic = False
            self.minpos = 0
            self.maxpos = size
            if(size > 0):
                for x in range(size):
                    self.mem.append(0)
        self.wrap = wrap
        self.maxint = maxint
        self.position = 0
        logger.info('Memory is (dynamic=%i, position=%i, maxpos=%i)' % (self.dynamic, self.position, self.maxpos))

    def Increase(self):
        if(self.wrap is True and self.mem[self.position] + 1 > self.maxint):
            logger.info('Memory increase (%i -> %i @ &%i)' % (self.mem[self.position], 0, self.position))
            self.mem[self.position] = 0
        else:
            logger.info('Memory increase (%i -> %i @ &%i)' % (self.mem[self.position], self.mem[self.position]+1, self.position))
            self.mem[self.position] += 1

    def Decrease(self):
        if(self.wrap is True and self.mem[self.position] - 1 < 0):
            logger.info('Memory decrease (%i -> %i @ &%i)' % (self.mem[self.position], self.maxint, self.position))
            self.mem[self.position] = self.maxint
        else:
            logger.info('Memory decrease (%i -> %i @ &%i)' % (self.mem[self.position], self.mem[self.position]-1, self.position))
            self.mem[self.position] -= 1

    def MoveRight(self):
        logger.info('Memory move right (&%i -> &%i)' % (self.position, self.position+1))
        if(self.dynamic is True):
            if(self.position+1 > self.maxpos):
                self.maxpos += 1
                self.mem.append(0)
        else:
            if(self.position+1 > self.maxpos):
                raise OutOfMemoryException(self.position + 1)
        self.position += 1

    def MoveLeft(self):
        logger.info('Memory move left (&%i -> &%i)' % (self.position, self.position+1))
        if(self.position - 1 < self.minpos):
            raise OutOfMemoryException(self.position - 1)
        self.position -= 1

    def GetCell(self):
        return self.mem[self.position]

    def SetCell(self, value):
        self.mem[self.position] = value
