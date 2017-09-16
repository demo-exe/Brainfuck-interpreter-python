from .log import logger

class IOutput:
    """Interface for accessing output"""
    def putNext(self, char):
        pass
    def flush(self):
        pass

class StdinOutput(IOutput):
    """Standard console output"""
    def putNext(self, char):
        logger.info("Putting char '%s'(%i)" % (chr(char), char))
        print(chr(char), end='')