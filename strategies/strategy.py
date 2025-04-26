import sys
sys.path.insert(0, '/home/feruiloba/quant-project/trees')

from abc import abstractmethod
from city import City
from nodes import Node

class Strategy():

    def __init__(
        self,
        city: City):

        # Initializing attributes
        self.city = city


    @abstractmethod
    def build_tree(self) -> Node:
        pass


