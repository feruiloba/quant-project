import json
from trees.nodes import TerminalNode, DecisionNode, ChanceNode, DecisionEdge, ChanceEdge

def create_decision_tree(file_name: str):
    # Parsing the JSON structure
    with open(file_name) as f:
        decision_tree_data = json.load(f)
        return create_node(decision_tree_data)

def create_chance_edges(node_data):
    cumulative_probability = 0
    sum_non_hashtag_probabilities = sum(eval(edge["probability"]) for edge in node_data["childEdges"] if edge["probability"] != "#")
    num_hashtags = len([edge for edge in node_data["childEdges"] if edge["probability"] == "#"])
    hashtag_probability = (1 - sum_non_hashtag_probabilities) / num_hashtags

    edges = []

    for edge in node_data["childEdges"]:

        edge_probability = edge["probability"]

        if edge_probability != "#":
            cumulative_probability += eval(edge_probability)

        edges.append(create_edge(edge, hashtag_probability))

    return edges

def create_edge(edge_data, hashtag_probability: float = None):
    edge_id = edge_data["id"]
    edge_name = edge_data["name"]
    edge_payoff = eval(str(edge_data["payoff"][0]))

    # Determine edge type
    if edge_data.get("probability") is None:
        edge = DecisionEdge(edge_name, edge_payoff, edge_id)
    else:
        edge_probability = eval(edge_data["probability"]) if edge_data["probability"] != "#" else hashtag_probability
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

    decision_tree = create_decision_tree("trees/Tree_with_updatedProb_Insurance.json")
    decision_tree.print_tree_vars()