class ISource:
    """Source parsing class interface"""

    def getToken(self, position):
        pass


class FileSource(ISource):
    """Parse file into source tokens""" #TODO: comments deleting, file virtualisation

    def __init__(self, filename):
        with open(filename,"r") as file:
            self.__text = file.read()

    def getToken(self, position):
        try:
            return self.__text[position]
        except:
            return 0