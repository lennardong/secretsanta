from fastapi import FastAPI
from src.graph_functional import SecretSantaGraph
from typing import List, Dict, Tuple, Union, Optional


app = FastAPI()

########################################
# Tinkering
########################################

@app.get("/")
async def root():
    return {
        "message": "Hello World"
    }

def test_func(input_variable):
    print("Inside test_func")  # Add a print statement
    return {
        "message": {input_variable} 
    }

@app.get("/test/{query}")
async def test_endpoint(query: int):
    return test_func(query)

########################################
# Implementation
########################################

santa = SecretSantaGraph()

@app.post("/relationships/add")
async def add_relationship(
    person1: str, 
    person2: str, 
    strength: float
    ):

    santa.add_relationship(person1, person2, strength)

    return {
        "message": "Relationship added successfully",
        "person1": person1,
        "person2": person2,
        "strength": strength,
    }

@app.post("/relationships/add/batch")
async def add_relationships(relationship_data: List[dict]):
  """
  Add multiple relationships in a single request.

  Args:
      relationship_data: A list of JSON objects, each containing the "person1", "person2", and "strength" keys.
    [
        {
            "person1": "Alice",
            "person2": "Bob",
            "strength": 0.8
        },
        {
            "person1": "Bob",
            "person2": "Charlie",
            "strength": 0.7
        },
        {
            "person1": "Charlie",
            "person2": "Alice",
            "strength": 0.6
        },
        // ... additional relationships
    ]

  Returns:
      A JSON object with a message and a list of successful and unsuccessful relationship additions.

  Raises:
      ValueError: If the number of relationships exceeds the limit or the data is invalid.
  """

  if len(relationship_data) > 100:
    raise ValueError("Maximum of 100 relationships allowed in a single request.")

  successful_additions = []
  failed_additions = []

  for relationship in relationship_data:
    try:
      person1 = relationship["person1"]
      person2 = relationship["person2"]
      strength = relationship["strength"]
      santa.add_relationship(person1, person2, strength)
      successful_additions.append({
          "person1": person1,
          "person2": person2,
          "strength": strength,
      })
    except Exception as e:
      failed_additions.append({
          "message": str(e),
          "person1": person1,
          "person2": person2,
      })

  return {
    "message": "Relationships added successfully.",
    "successful_additions": successful_additions,
    "failed_additions": failed_additions,
  }



"""
Typecasting via hints happen at decorated function

"""