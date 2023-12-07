from src.graph_functional import SecretSantaGraph
import pytest
from typing import List, Tuple


def test_add_node():
    """Tests adding a new node to the graph."""

    # Create a graph instance
    graph = SecretSantaGraph()

    # Add a new node
    node = graph.add_node("John")

    # Verify the node exists in the graph
    assert node in graph._nodes.keys()


def test_add_relationship():
    """Tests adding a relationship between two nodes in the graph."""

    # Create a graph instance
    graph = SecretSantaGraph()

    # Add two nodes
    node_a = graph.add_node("Alice")
    graph.add_node(node_a)
    node_b = graph.add_node("Bob")
    graph.add_node(node_b)

    # Add a relationship
    temperature = 0.7
    graph.add_relationship(node_a, node_b, temperature)

    # Verify the relationship exists
    relationship = graph._nodes[node_a.name][0]
    assert relationship.name == node_b.name
    assert relationship.temperature == temperature


def test_get_valid_relationships():
    """Tests retrieving valid relationships based on temperature range."""

    # Create a graph instance
    graph = SecretSantaGraph()

    # Add two nodes and a relationship
    node_a = graph.add_node("Alice")
    graph.add_node(node_a)
    node_b = graph.add("Bob")
    graph.add_node(node_b)
    graph.add_relationship(node_a, node_b, 0.5)

    # Get valid relationships
    lower_bound = 0.4
    upper_bound = 0.6
    valid_relationships = graph._get_valid_relationships(node_a, lower_bound, upper_bound)

    # Verify only the valid relationship is returned
    assert len(valid_relationships) == 1
    assert valid_relationships[0].name == node_b.name and valid_relationships[0].temperature == 0.5


def test_generate_pairs_valid():
    """Tests generating valid pairs with specified temperature range."""

    # Create a graph instance
    graph = SecretSantaGraph()

    # Add nodes and relationships
    node_a = PersonNode("Alice")
    graph.add_node(node_a)
    node_b = PersonNode("Bob")
    graph.add_node(node_b)
    node_c = PersonNode("Charlie")
    graph.add_node(node_c)
    node_d = PersonNode("David")
    graph.add_node(node_d)

    graph.add_relationship(node_a, node_b, 0.7)
    graph.add_relationship(node_a, node_c, 0.5)
    graph.add_relationship(node_b, node_c, 0.4)
    graph.add_relationship(node_b, node_d, 0.6)
    graph.add_relationship(node_c, node_d, 0.8)

    # Generate pairs with valid range
    lower_bound = 0.4
    upper_bound = 0.6
    pairs = graph.generate_pairs(lower_bound, upper_bound)

    # Verify pairs are valid and all nodes are assigned
    assert len(pairs) == 3
    for pair in pairs:
        donor, recipient = pair
        assert graph.has_valid_relationship(donor, recipient, boundaries=(lower_bound, upper_bound))
    assigned_nodes = set(donor for donor, _ in pairs) | set(recipient for _, recipient in pairs)
    assert assigned_nodes == {node_a, node_b, node_c, node_d}


def test_generate_pairs_no_valid_receivers():
    """Tests generating pairs when no valid receivers exist for a giver."""

    # Create a graph instance
    graph = SecretSantaGraph()

    # Add nodes and relationships with conflicting preferences
    node_a = PersonNode("Alice")
    graph.add_node(node_a)
    node_b = PersonNode("Bob")
    graph.add_node(node_b)
    node_c = PersonNode("Charlie")
    graph.add_node(node_c)
    node_d = PersonNode("David")
    
