import random
import matplotlib.pyplot as plt
from collections import defaultdict
from typing import Optional, Tuple, Dict


class Node:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name


class Edge:
    def __init__(self, from_node: Node, to_node: Node, weight: float):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight

    def __str__(self):
        return f"{self.from_node.name} -> {self.to_node.name} ({self.weight})"
    

class Graph:
    def __init__(self):
        self.nodes = {}  # {name: Node}
        self.edges = set()

    def __iter__(self):
        return iter(self.nodes.values())
    
    def __str__(self):
        output = ""
        for node in self:
            output += f"{node.name}: "
            for edge in self.edges:
                if edge.from_node == node:
                    output += f"{edge.to_node.name} ({edge.weight:.2f}), "
            output = output.rstrip(", ")

    def add_node(self, node: Node):
        self.nodes[node.name] = node

    def add_edge(self, from_node: Node, to_node: Node, weight: float):
        edge = Edge(from_node, to_node, weight)
        self.edges.add(edge)

    def get_relationship(self, node1: Node, node2: Node) -> Optional[float]:
        for edge in self.edges:
            if edge.from_node == node1 and edge.to_node == node2:
                return edge.weight
        return None

    def get_relationships(self, node: Node, lower: float = 0.0, upper: float = 1.0):
        """Returns a list of valid relationships for a node within the upper and lower bounds"""
        valid_relationships = []
        for edge in self.edges:
            if edge.from_node == node:
                if edge.weight < upper and edge.weight > lower:
                    valid_relationships.append(edge.to_node)
        return valid_relationships

    def generate_pairs(self, threshold: Tuple[float, float]):
        """Generates Secret Santa assignments based on relationship scores and threshold"""
        assignments = {}

        # Iterate through each node
        for node in self:
            # Get valid relationships within the threshold
            valid_relationships = self.get_relationships(node, *threshold)

            # Choose a recipient at random
            # Implement your desired matching algorithm here (e.g., maximum score matching)
            recipient = random.choice(valid_relationships)

            # Assign recipient and avoid assigning the same person to themselves
            if recipient != node:
                assignments[node.name] = recipient.name

        return assignments


# create an prompt for user input to create participants.

############################################
# MAIN
############################################

if __name__ == "__main__":
    print("Welcome to the Secret Santa Generator!")

    # Create Nodes
    graph = Graph()

    while True:
        name = input("Enter participant name: (type 'y' to finish)")
        if name == "y":
            break
        try:
            graph.add_node(Node(name))
            print(f"... Added {name} to Secret Santa Pool.")
        except:
            print("Invalid input. Please try again.")

    # Create Edges
    print("Lets go through the pool and add relationships.")
    # for each participant, show a list with input. If person added, it means its a skip
    for node1 in graph:
        print(f"Adding relationships for {node1.name}")

        for node2 in graph:
            if node2 == node1:
                continue

            score = input(f"Enter score for {node2.name} (0 (cold) - 1 (warm)): ")
            try:
                score = float(score)
                graph.add_edge(node1, node2, score)
            except:
                print("Invalid input. Please try again.")

    # Generate and print Secret Santa assignments
    assignments = graph.generate_pairs((0.5, 1.0))
    print("Secret Santa Assignments:")
    for giver, recipient in assignments.items():
        print(f"{giver} -> {recipient}")


# ############################################
# # GRAPH APPROACH
# ############################################

# import networkx as nx
# import matplotlib.pyplot as plt
# from collections import defaultdict
# from typing import Optional, Tuple, Dict

# class Participant:
#     def __init__(self, name):
#         self.name = name
#         self.relationships = defaultdict(lambda: 0.0)  # {other_participant: score}

#     def __repr__(self) -> Tuple[str, Dict[str, float]]:
#         return self.name, self.relationships

#     def __str__(self) -> str:
#         output = f"{self.name}: "
#         for other_participant, score in self.relationships.items():
#             output += f"({other_participant.name}, {score:.2f}), "
#         return output.rstrip(", ")  # remove trailing comma and space

#     def add_relationship(self, other_participant: Participant, score: float):
#         self.relationships[other_participant] = score

#     def get_valid_relationships(self, lower: float, upper: float):
#         """Returns a list1
#          of relationships that are within the upper and lower bounds
#         """
#         relationships = []
#         for other_participant, score in self.relationships.items():
#             if score < upper and score > lower:
#                 relationships.append(other_participant)
#         return relationships

# # TODO look in to __repr__ and __str__ for the classes
# # graph.participants should show a list of all participants

# class SocialGraph:
#     def __init__(self):
#         self.participants = []  # {name: Participant}

#     def __str__(self) -> str:
#         # Show all participants and their relationships
#         output = ""
#         for participant in self.participants:
#             output += f"{participant}\n"
#         return output

#     def __iter__(self):
#         for participant in self.participants:
#             yield participant

#     def add_participant(self, participant: Participant):
#         participant = Participant(name)
#         self.participants.append(participant)

#     def create_graph(self, threshold: Tuple[float, float]):
#         """

#         Returns: ???
#         """
#         for participant in self.participants:
#             relationships = participant.get_valid_relationships(*threshold)
#             for relationship in relationships:


# # create an prompt for user input to create participants.
# if __name__ == "__main__":
#     print("Welcome to the Secret Santa Generator!")

#     # Create Nodes
#     participants = []
#     graph = SocialGraph()
#     while True:
#         name = input("Enter participant name: (type 'y' to finish)")
#         if name == "y":
#             break
#         try:
#             graph.add_participant(name)
#             print(f"... Added {name} to Secret Santa Pool.")
#         except:
#             print("Invalid input. Please try again.")

#     # Create Edges
#     print("Lets go through the pool and add relationships.")
#     # for each participant, show a list with input. If person added, it means its a skip
#     for participant in graph:
#         print(f"Adding relationships for {participant.name}")

#         for other_participant in graph:
#             if other_participant.name == participant.name:
#                 continue

#             score = input(f"Enter score for {other_participant.name} (0 (cold) - 1 (warm)): ")
#             try:
#                 score = float(score)
#                 participant.add_relationship(other_participant, score)
#             except:
#                 print("Invalid input. Please try again.")
