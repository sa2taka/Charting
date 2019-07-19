from container import Cotainer
from memory_container import MemoryContainer

class CandleCreator:
    def __init__(self, containerClass = MemoryContainer):
        if not issubclass(containerClass, Container):
            raise TypeError
        self.container = containerClass

    def 
