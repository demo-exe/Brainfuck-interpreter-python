import re

class ISource:
    """Source parsing class interface"""

    def getToken(self, position):
        pass

    def _removeComments(self, string):
        string = string.replace("\n", "")
        return re.sub(r'[^.,+-<>\[\]]', '', string)



class FileSource(ISource):
    """Parse file into source tokens""" #TODO: comments deleting, file virtualisation

    def __init__(self, file):
        self.__text = file.read()

        self.__text = self._removeComments(self.__text)
        

    def getToken(self, position):
        try:
            return self.__text[position]
        except:
            return 0