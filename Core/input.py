from .log import logger

class IInput:
    """Interface for accessing input"""
    def __init__(self):
        logger.debug('Constructing base IInput ')
        self._position = 0
        self._inputtext = ''

    def getNext(self):
        try:
            ch = self._inputtext[self._position]
            self._position += 1
            logger.info("Getting '%c'[%i] (%i/%i) " % (ch, ord(ch), self._position, len(self._inputtext)))
            return ord(ch)
        except: #todo catch only key?exception
            logger.info('Getting zero')
            return 0

class StdinInput(IInput):
    """Standard console input""" #TODO: implement program-blocking input
    def __init__(self):
        super().__init__()
        logger.debug('Constructing StdinInput')
        self._inputtext = input("Please specify input for a program: ")
        logger.info('Input received: %s' % self._inputtext)
    
class StringInput(IInput):
    def __init__(self, input_string):
        super().__init__()
        logger.debug('Constructing StringInput')
        self._inputtext = input_string
        logger.info('Input received: %s' % self._inputtext)