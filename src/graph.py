import random
from dataclasses import dataclass, field
from typing import Dict, Tuple, List, Optional, Union


@dataclass
class PersonNode:
    """Object with person attributes and relationshpis with scores"""

    name: str
    edgeList: List[Tuple[Optional["PersonNode"], float]] = field(default_factory=list)
    preferences: list = field(default_factory=list)
    aversions: list = field(default_factory=list)

    def add_preference(self, item):
        self.preferences.append(item)

    def add_aversion(self, item):
        self.aversions.append(item)

    def add_relationship(self, person: "PersonNode", temperature: float = 1.0):
        self.edgeList.append((person, temperature))


class SecretSantaGraph:
    def __init__(self):
        self.nodes = {}  # {name: PersonNode}

    def add_node(self, name: str) -> Dict[str, PersonNode]:
        node = PersonNode(name)
        self.nodes[node.name] = node
        return self.nodes[node.name]

    def add_edge(
        self,
        from_node: Union[str, PersonNode],
        to_node: Union[str, PersonNode],
        temperature: float = 1.0,
    ) -> Tuple[PersonNode, PersonNode, float]:
        # Typecast
        if isinstance(from_node, str):
            from_node = self.nodes[from_node]
        if isinstance(to_node, str):
            to_node = self.nodes[to_node]

        from_node.add_relationship(to_node, temperature)

        return from_node, to_node, temperature

    def get_valid_relationships(
        self, node: Union[PersonNode, str], boundaries: Tuple[float, float] = (0, 1)
    ) -> List[Tuple[PersonNode, float]]:
        """Returns a list of valid relationships for a node within upper and lower bounds"""
        # Typecast
        if isinstance(node, str):
            node = self.nodes[node]

        valid_relationships = []
        for edge in node.edgeList:  # (PersonNode, float)
            _node, _temp = edge
            if (_temp >= boundaries[0]) and (_temp < boundaries[1]):
                valid_relationships.append((_node, _temp))

        return valid_relationships

    def generate_pairs(
        self,
        lower: float = 0,
        upper: float = 1,
    ) -> List[Tuple[PersonNode, PersonNode]]:
        """Generates a list of valid pairs based on temperature boundaries using BFS."""

        assigned = set()
        pairs = []  # List to store generated pairs
        queue = []  # Queue for BFS traversal

        # Add all nodes with valid relationships within the desired temperature range to the queue.
        for node in self.nodes.values():
            valid_relationships = self.get_valid_relationships(
                node, boundaries=(lower, upper)
            )
            if valid_relationships:
                queue.append((node, valid_relationships))

        # Perform BFS traversal
        while queue:
            current_node, relationships = queue.pop(0)

            # Check if the current node hasn't been assigned yet.
            if current_node.name not in assigned:
                assigned.add(current_node.name)

                # Select a random valid relationship.
                random_relationship = random.choice(relationships)
                related_node, temperature = random_relationship

                # Add the valid pair to the results.
                pairs.append((current_node, related_node, temperature))

                # Add the related node to the queue if it hasn't been assigned and has valid relationships.
                if (related_node.name not in assigned) and (
                    self.get_valid_relationships(
                        related_node, boundaries=(lower, upper)
                    )
                ):
                    queue.append(
                        (
                            related_node,
                            self.get_valid_relationships(
                                related_node, boundaries=(lower, upper)
                            ),
                        )
                    )

        return pairs

    def generate_pairs_v1(
        self,
        lower: float = 0,
        upper: float = 1,
    ) -> List[Tuple[PersonNode, PersonNode]]:
        """Returns a list of pairs"""

        assigned = set()
        pairs = list()
        queue = list()

        # implement BFS to find valid pairs

        for node in self.nodes.values():
            valid_relationships = self.get_valid_relationships(
                node, boundaries=(lower, upper)
            )
            if valid_relationships:
                queue.append(
                    (node, valid_relationships)
                )  # [(person, [(person, temp), (person, temp)]), ...]

        while queue:
            node_curr, relationships = queue.pop(0)

            if node_curr.name in assigned:
                continue

            # Log
            assigned.add(node_curr.name)

            # Select a random valid relationship
            node_adj, temp = random.choice(relationships)  # (person, temp)

            # Add valid pair to results
            pairs.append((node_curr, node_adj))

            # add next node to q if it hasn't been assigned and has valid relationships
            if node_adj.name not in assigned:
                valid_relationships = self.get_valid_relationships(
                    node_adj, boundaries=(lower, upper)
                )
                if valid_relationships:
                    queue.append((node_adj, valid_relationships))

        return pairs
