from collections import namedtuple, deque, defaultdict
from dataclasses import dataclass
import random


@dataclass(frozen=True)
class Relationship:
    name: str
    temperature: float = 1.0


class SecretSantaGraph:
    def __init__(self):
        self._nodes = defaultdict(list)  # name: [(name, temp), ...]

    def add_node(self, name: str):
        self._nodes[name] = []

    def add_relationship(self, from_node: str, to_node: str, temperature: float):
        if from_node not in self._nodes:
            self.add_node(from_node)
        temperature = 1.0 if temperature > 1.0 else temperature
        temperature = 0.0 if temperature < 0.0 else temperature

        self._nodes[from_node].append(Relationship(to_node, temperature))
        return self._nodes[from_node]

    def get_valid_relationships(
        self, name: str, lower: float = 0.0, upper: float = 1.0
    ):
        return [
            r
            for r in self._nodes[name]
            if lower <= r.temperature and r.temperature < upper
        ]

    def generate_pairs(self, lower: float = 0, upper: float = 1.0):
        assigned_receiver = set()
        assigned_gifter = set()
        queue = deque(self._nodes.keys())
        pairs = []

        while queue:
            giver = queue.popleft()

            valid_relationships = set(self.get_valid_relationships(giver, lower, upper))
            valid_receivers = list(valid_relationships - assigned_receiver)

            # Defensive checks
            if giver in assigned_receiver:
                continue

            if valid_receivers is None:
                print("No valid receiviers")
                break

            receiever = random.choice(valid_receivers).name
            while receiever in assigned_gifter:
                receiever = random.choice(valid_receivers).name

            pairs.append((giver, receiever))
            assigned_receiver.add(giver)
            assigned_gifter.add(receiever)

        return pairs


############################################
# Sample
############################################

if __name__ == "__main__":
    santa = SecretSantaGraph()

    # Step 1: Add all participants
    santa.add_node("Alice")
    santa.add_node("Bob")
    santa.add_node("Charlie")
    santa.add_node("David")

    # Step 2: Create relationships between participants
    santa.add_relationship("Alice", "Bob", 0.8)
    santa.add_relationship("Alice", "Charlie", 0.5)
    santa.add_relationship("Alice", "David", 7.7)

    santa.add_relationship("Bob", "Alice", 0.8)
    santa.add_relationship("Bob", "Charlie", 0.3)
    santa.add_relationship("Bob", "David", 0.6)

    santa.add_relationship("Charlie", "Alice", 0.4)
    santa.add_relationship("Charlie", "Bob", 0.4)
    santa.add_relationship("Charlie", "David", 0.8)

    santa.add_relationship("David", "Alice", 0.5)
    santa.add_relationship("David", "Bob", 0.6)
    santa.add_relationship("David", "Charlie", 0.7)

    # Generate pairs with temperature range 0.5 to 0.8
    pairs = santa.generate_pairs(lower=0, upper=0.8)
    print(pairs)
