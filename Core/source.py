from .log import logger
import re

class ISource:
    """Source parsing class interface"""

    def getToken(self, position):
        pass

    def _removeComments(self, string):
        logger.debug("Umcommenting code")
        string = string.replace("\n", "")
        tmp = re.sub(r'[^.,+-<>\[\]]', '', string)
        logger.info("Code without comments: %s" % (tmp))
        return tmp



class FileSource(ISource):
    """Parse file into source tokens""" #TODO: comments deleting, file virtualisation

    def __init__(self, file):
        logger.debug("Reading file")
        self.__text = file.read()

        self.__text = self._removeComments(self.__text)
        

    def getToken(self, position):
        try:
            logger.debug("Source returing '%s' from position (%i)" % (self.__text[position], position)) 
            return self.__text[position]
        except:
            logger.debug("EOF?: Source returing '0' from position (%i)" % (position)) 
            return 0