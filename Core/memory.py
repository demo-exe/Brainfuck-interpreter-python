class OutOfMemoryException(Exception):
    def __init__(self, mem_index=None):
        if(mem_index == None):
            super().__init__()
        else:
            super().__init__('Error at index : %i' % mem_index)



class Memory:
    def __init__(self, size=30000, 
                       wrap=True, maxint=256):
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

    def Increase(self):
        if(self.wrap is True and self.mem[self.position] + 1 > self.maxint):
            self.mem[self.position] = 0
        else:
            self.mem[self.position] += 1

    def Decrease(self):
        if(self.wrap is True and self.mem[self.position] - 1 < 0):
            self.mem[self.position] = self.maxint
        else:
            self.mem[self.position] -= 1

    def MoveRight(self):
        if(self.dynamic is True):
            if(self.position+1 > self.maxpos):
                self.maxpos += 1
                self.mem.append(0)
        else:
            if(self.position+1 > self.maxpos):
                raise OutOfMemoryException(self.position + 1)
        self.position += 1

    def MoveLeft(self):
        if(self.position - 1 < self.minpos):
            raise OutOfMemoryException(self.position - 1)
        self.position -= 1

    def GetCell(self):
        return self.mem[self.position]

    def SetCell(self, value):
        self.mem[self.position] = value
