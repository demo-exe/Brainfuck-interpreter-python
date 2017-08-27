class Memory:
    def __init__(self):
       self.mem = []
       for i in range(30000):
           self.mem.append(0)
       self.position = 0
    def Increase(self):
        self.mem[self.position] += 1

    def Decrease(self):
        self.mem[self.position] -= 1

    def MoveRight(self):
        self.position += 1

    def MoveLeft(self):
        self.position -= 1

    def GetCell(self):
        return self.mem[self.position]

    def SetCell(self, value):
        self.mem[self.position] = value