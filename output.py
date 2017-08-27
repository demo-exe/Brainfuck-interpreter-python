class IOutput:
    """Interface for accessing output"""
    def putNext(self, char):
        pass
    def flush(self):
        pass

class StdinOutput(IOutput):
    """Standard console output"""
    def putNext(self, char):
        print(char, end='')