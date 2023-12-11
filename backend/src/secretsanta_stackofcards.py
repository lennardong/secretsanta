"""
Secret Santa Matching
- simple secret standa matching algorithm
- no duplicate giftees, accounts for "excludes"
"""

import random
from pprint import pprint

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

giftee_pool = list(names.keys())
result = []  # [(gifter, giftee)]

for gifter, excludes in names.items():

    # Randomly select from pool with conditions
    giftee = random.choice(giftee_pool)
    while (giftee in excludes) or (giftee == gifter):
        giftee = random.choice(giftee_pool)

    # Generate result
    result.append((gifter, giftee))
    giftee_pool.remove(giftee)

pprint(result)

for gifter, giftee in result:
    print(f"🥷Your Secret Santa: {gifter} -> {giftee} (👍 to accept)")


