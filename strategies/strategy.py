
from abc import abstractmethod
from strategies.city import City
from trees.nodes import ChanceEdge, ChanceNode, DecisionEdge, DecisionNode, Node, TerminalNode

class Strategy():

    def __init__(
        self,
        city: City):

        # Initializing attributes
        self.city = city


    @abstractmethod
    def build_tree(self) -> Node:
        pass


