"""
Secret Santa Matching
- simple secret standa matching algorithm
- no duplicate giftees, accounts for "excludes"
"""

import random
from pprint import pprint
from typing import Dict, List, Tuple, Optional, Union


def generate_secretSanta(
        names: Dict[str, List[str]]
        ) -> List[Tuple[str, str]]:
    """
    Generate a list of secret santa matches from a dictionary of names and exclusions.
    """
    giftee_pool = list(names.keys())
    result = []  # [(gifter, giftee), ...]

    # Sort input dictionary by number of excludes, with most excludes first
    names = {k: v for k, v in sorted(names.items(), key=lambda item: len(item[1]), reverse=True)}

    for gifter, excludes in names.items():

        # Randomly select from pool with conditions
        giftee = random.choice(giftee_pool)
        while (giftee in excludes) or (giftee == gifter):
            giftee = random.choice(giftee_pool)

        # Generate result
        result.append((gifter, giftee))
        giftee_pool.remove(giftee)
    
    return result

if __name__ == "__main__":
    names = {
        "Clive": ["Alma", "Amy"],
        "Alma": ["Clive", "Amy"],
        "Andrew": ["Emma", "Evelyn", "William"],
        "Emma": ["Andrew", "Evelyn", "William"],
        "Lennard": ["Lara", "Leah", "Maya"],
        "Lara": ["Lennard", "Leah", "Maya"],
        "Wayne": ["Amy"],
        "Amy": ["Wayne", "Clive", "Alma"],
        "Annie": [],
        "Leah": ["Lennard", "Lara", "Maya"],
        "Maya": ["Lennard", "Lara", "Leah"],
        "William": ["Andrew", "Emma", "Evelyn"],
        "Evelyn": ["Andrew", "Emma", "William"],
    }  # {gifter: [gifteesToAvoid]}
    
    result = generate_secretSanta(names)
    pprint(result)

    for gifter, giftee in result:
        print(f"🥷Your Secret Santa: {gifter} -> {giftee} (👍 to accept)")


