import json
from nodes import TerminalNode, DecisionNode, ChanceNode, DecisionEdge, ChanceEdge

def create_decision_tree(file_name: str):
    # Parsing the JSON structure
    with open(file_name) as f:
        decision_tree_data = json.load(f)
        main_node = create_node(decision_tree_data)
        main_node.print_tree()

def create_chance_edges(node_data):
    cumulative_probability = 0
    num_hashtags = len([edge for edge in node_data["childEdges"] if edge["probability"] == "#"])

    edges = []

    for edge in node_data["childEdges"]:
        cumulative_probability += float(edge["probability"]) if edge["probability"] != "#" else 0
        edges.append(create_edge(edge, cumulative_probability, num_hashtags))

    return edges

def create_edge(edge_data, cumulative_probability: float = None, num_hashtags: int = 0):
    edge_id = edge_data["id"]
    edge_name = edge_data["name"]
    edge_payoff = float(edge_data["payoff"][0])

    # Determine edge type
    if edge_data.get("probability") is None:
        edge = DecisionEdge(edge_name, edge_payoff, edge_id)
    else:
        edge_probability = float(edge_data["probability"]) if edge_data["probability"] != "#" else ((1 - cumulative_probability) / num_hashtags)
        edge = ChanceEdge(edge_name, edge_payoff, edge_probability, edge_id)

    if edge_data["childNode"] is not None:
        edge.result_node = create_node(edge_data["childNode"])

    return edge

def create_node(node_data):
    node_id = node_data["id"]
    node_name = node_data["name"]

    # Determine node type
    if node_data["type"] == "terminal":
        return TerminalNode(node_name, node_id)
    elif node_data["type"] == "decision":
        edges = [create_edge(edge) for edge in node_data["childEdges"]]
        return DecisionNode(node_name, edges, id=node_id)
    elif node_data["type"] == "chance":
        edges = create_chance_edges(node_data)
        return ChanceNode(node_name, edges, id=node_id)
    else:
        raise ValueError(f"Unknown node type: {node_data['type']}")


if __name__ == "__main__":

    decision_tree = create_decision_tree("trees/decisiontree@2025.04.20_20.39.38.json")