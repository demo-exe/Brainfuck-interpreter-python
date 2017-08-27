class IInput:
    """Interface for accessing input"""
    def getNext(self):
        pass

class StdinInput(IInput):
    """Standard console input""" #TODO: implement program-blocking input
    def __init__(self):
        self.__position = 0
        self.__inputtext = input("Please specify input for a program: ")

    def getNext(self):
        try:
            ch = self.__inputtext[self.__position]
            self.__position += 1
            return ord(ch)
        except: #todo catch only key?exception
            return 0