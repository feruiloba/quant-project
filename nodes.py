from abc import abstractmethod
import uuid

def get_lower_case_no_dash(text: str):
    return text.lower().strip().replace(" ", "_").replace("-", "_").replace("?", "").replace("'", "").replace("(", "").replace(")", "").replace(",", "_")

def get_var_name(text: str):
    guid = str(uuid.uuid4())[0:5]
    full_var_name = f"{text}_{guid}"

    return get_lower_case_no_dash(full_var_name)

class Node():
    def __init__(self, name: str, id: str = None):
        self.id = id
        self.name = name

    @abstractmethod
    def get_payoff(self):
        pass

    def get_var_name(self):
        return get_var_name(self.name)

    def print_tree_vars(self, level=0, result_nodes: list[str] = []):

        if self.id == None:
            self.id = self.get_var_name()

        edge_vars = []
        if hasattr(self, "edges"):
            for edge in self.edges:

                if edge.id is None:
                    edge.id = edge.get_var_name()

                edge_var_name = f"edge_{edge.get_var_name()}"
                edge_vars.append(edge_var_name)

                if type(edge) is DecisionEdge:
                    print(f"{edge_var_name} = DecisionEdge(name='{edge.get_var_name()}', payoff={edge.payoff}, id='{edge.id}')")
                elif type(edge) is ChanceEdge:
                    print(f"{edge_var_name} = ChanceEdge(name='{edge.get_var_name()}', payoff={edge.payoff}, probability={edge.probability}, id='{edge.id}')")

                if edge.result_node:
                    if edge.result_node.id is None:
                        edge.result_node.id = edge.result_node.get_var_name()
                    result_nodes.append(f"{edge_var_name}.result_node = node_{get_lower_case_no_dash(edge.result_node.id)}")
                    edge.result_node.print_tree_vars(level + 1, result_nodes)

        edge_names = ", ".join(edge_vars)
        if type(self) is ChanceNode:
            print(f"node_{get_lower_case_no_dash(self.id)} = ChanceNode(name='{self.get_var_name()}', id='{self.id}', edges=[{edge_names}])")
        elif type(self) is DecisionNode:
            print(f"node_{get_lower_case_no_dash(self.id)} = DecisionNode(name='{self.get_var_name()}', id='{self.id}', edges=[{edge_names}])")
        elif type(self) is TerminalNode:
            print(f"node_{get_lower_case_no_dash(self.id)} = TerminalNode(name='{self.get_var_name()}', id='{self.id}')")

        if level == 0:
            print("\n".join(result_nodes))

    def print_tree(self, level=0):
        indent = "  " * level
        if (type(self) != TerminalNode):
            print(f"{indent}Node: {self.name}. Payoff {self.get_payoff()}")

        if hasattr(self, 'edges'):
            for edge in self.edges:
                result_node_name = edge.result_node.name if edge.result_node and edge.result_node.name != '' else "Terminal"
                print(f"{indent}  Edge: {edge.name} -> {result_node_name}. Payoff: {edge.get_payoff()}")
                if edge.result_node:
                    edge.result_node.print_tree(level + 1)

class Edge():
    def __init__(self, name: str, payoff: float, result_node: Node = None, id: str = None):
        self.id = id
        self.name = name
        self.payoff = payoff
        self.result_node = result_node

    def get_payoff(self):
        if self.result_node == None:
            return self.payoff

        return self.payoff + self.result_node.get_payoff()

    def get_var_name(self):
        return get_var_name(self.name)

class DecisionEdge(Edge):
    def __init__(self, name: str, payoff: float, id: str = None):
        super().__init__(name, payoff, id=id)

class ChanceEdge(Edge):
    def __init__(self, name: str, payoff: float, probability: float, id: str = None):
        super().__init__(name, payoff, id)
        self.probability = probability

    def get_payoff(self):
        payoff = self.payoff

        if self.result_node != None:
            payoff += self.result_node.get_payoff()

        return self.probability * payoff

class DecisionNode(Node):
    def __init__(self, name, edges: list[DecisionEdge], override_decision: str = None, id: str = None):
        super().__init__(name, id)
        self.edges = edges
        self.override_decision = override_decision

    def get_payoff(self):
        if self.override_decision != None:
            return next((edge.get_payoff() for edge in self.edges if edge.name == self.override_decision), 0)

        return max(edge.get_payoff() for edge in self.edges)

class ChanceNode(Node):
    def __init__(self, name, edges: list[ChanceEdge], id: str = None):
        super().__init__(name, id)
        if len(edges) == 0:
            raise ValueError("ChanceNode must have at least one edge")

        total_probability = sum(edge.probability for edge in edges)

        if total_probability != 1:
            raise ValueError(f"Total probability must be 1, but got {total_probability}. Name: {name}")

        super().__init__(name)
        self.edges = edges

    def get_payoff(self):
        return sum(edge.get_payoff() for edge in self.edges)

class TerminalNode(Node):
    def __init__(self, name, id: str = None):
        super().__init__(name, id)

    def get_payoff(self):
        return 0

if __name__ == "__main__":
    zod_attack_yes = ChanceEdge("Yes Zod Attack", 0, 0.2)
    zod_attack_no = ChanceEdge("No Zod Attack", 0, 0.8)
    zod_attack_node = ChanceNode("Zod Attack?", [zod_attack_yes, zod_attack_no])

    superman_hire_yes = DecisionEdge("Hire Superman", -32500000)
    superman_hire_no = DecisionEdge("No Superman", -50000000)
    superman_hire_node = DecisionNode("Hire Superman?", [superman_hire_yes, superman_hire_no])
    zod_attack_yes.result_node = superman_hire_node

    batman_hire_yes = DecisionEdge("Hire Batman", -10000000)
    batman_hire_no = DecisionEdge("Don't hire Batman", 0)
    batman_hire_node = DecisionNode("Hire Batman?", [batman_hire_yes, batman_hire_no])
    zod_attack_no.result_node = batman_hire_node

    joker_attack_yes = ChanceEdge("Yes Joker Attack", -1500000, 0.5)
    joker_attack_no = ChanceEdge("No Joker Attack", 0, 0.5)
    joker_attack_node = ChanceNode("Joker Attack?", [joker_attack_yes, joker_attack_no])
    batman_hire_yes.result_node = joker_attack_node

    no_batman_joker_attack_yes = ChanceEdge("No BM Yes Joker Attack", -30000000, 0.5)
    no_batman_joker_attack_no = ChanceEdge("No BM No Joker Attack", 0, 0.5)
    no_batman_joker_attack_node = ChanceNode("No BM. Joker Attack?", [no_batman_joker_attack_yes, no_batman_joker_attack_no])
    batman_hire_no.result_node = no_batman_joker_attack_node

    no_batman_joker_attack_no.result_node = TerminalNode(id="9bd785f6-e6fc-af5c-3eb9-b79e0d029cd7", name="Terminal")

    print(zod_attack_node.get_payoff())
