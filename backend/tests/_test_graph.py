from src.graph import SecretSantaGraph, PersonNode
import pytest
from typing import List, Tuple


def test_add_node():
    """Tests adding a new node to the graph."""

    # Create a graph instance
    graph = SecretSantaGraph()

    # Add a new node
    node = graph.add_node("John")

    # Verify the node exists in the graph
    assert node in graph.nodes.values()
    assert graph.nodes["John"] == node

def test_add_edges():
    """Tests adding edges to graph
    """

    # create 2 nodes A-B
    graph = SecretSantaGraph()
    node_a = graph.add_node("Adam")
    node_b = graph.add_node("Ben")
    temp = 0.5

    # add edge
    n_source, n_dest, temp = graph.add_edge(node_a, node_b, temp)

    # get relationship
    relationships = graph.get_valid_relationships(node_a)

    # assert
    assert n_source == node_a
    assert n_dest == node_b
    assert (node_b, temp) in relationships

def test_generate_pairs():
    """Tests generating pairs of people for Secret Santa."""

    # Create a graph instance
    graph = SecretSantaGraph()

    # Add nodes to the graph
    node_a = graph.add_node("Alice")
    node_b = graph.add_node("Bob")
    node_c = graph.add_node("Charlie")
    node_d = graph.add_node("David")

    # Add edges to the graph
    graph.add_edge(node_a, node_b, 0.5)
    graph.add_edge(node_b, node_c, 0.7)
    graph.add_edge(node_c, node_d, 0.55)
    graph.add_edge(node_d, node_a, 0.8)

    # Generate pairs
    pairs = graph.generate_pairs(lower=0.4, upper=0.6)
    print(pairs)

    # Verify the generated pairs
    assert len(pairs) == 2
    assert (node_a, node_b) in pairs or (node_b, node_a) in pairs
    assert (node_c, node_d) in pairs or (node_d, node_c) in pairs

    # Verify that all nodes are assigned
    assigned_nodes = set()
    for pair in pairs:
        assigned_nodes.add(pair[0])
        assigned_nodes.add(pair[1])
    assert assigned_nodes == {node_a, node_b, node_c, node_d}

    # Verify that all pairs have valid relationships
    for pair in pairs:
        assert graph.has_valid_relationship(pair[0], pair[1], boundaries=(0.4, 0.6))