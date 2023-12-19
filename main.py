# Misc
from dataclasses import Field
from typing import List, Dict, Tuple, Union, Optional

# FastAPi
from fastapi import FastAPI, Body, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
# from fastapi.middleware.cors import CORSMiddleware

# Project Files
from core.stack import generate_secretSanta
from core.graph_functional import SecretSantaGraph

# INIT
app = FastAPI()

########################################
# Tinkering
########################################

@app.get("/")
async def root():
    return {"message": "Hello World"}

# FIXME: get routing for static files working
# @app.get("/")
# async def home():
#     return FileResponse("static/index.html")


def test_func(input_variable):
    print("Inside test_func")  # Add a print statement
    return {"message": {input_variable}}

@app.get("/test/{query}")
async def test_endpoint(query: int):
    return test_func(query)


########################################
# Implementation: Stack
########################################
# Configure CORS for local dev
# note - This can be removed because the frontend and backend are served from the same origin
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],  # Allows all origins
#     allow_credentials=True,
#     allow_methods=["*"],  # Allows all methods
#     allow_headers=["*"],  # Allows all headers
# )

class SecretSantaInput(BaseModel):
    """
    Pydantic model for a secret santa request.
    """
    names: Dict[str, List[str]]


@app.post("/api/secret-santa-stack/")
async def generate_secret_santa(input: SecretSantaInput):
    """
    Generate a list of secret santa matches from a dictionary of names and exclusions.
    """
    try:
        names = input.names
        return generate_secretSanta(names)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

app.mount("/static", StaticFiles(directory="./frontend/dist/", html=True), name="static")  # Serve the static HTML file
app.mount("/assets", StaticFiles(directory="./frontend/dist/assets"))  # enable the route for static assets

########################################
# Implementation: Graph
########################################

# santa = SecretSantaGraph()


# class RelationshipCreation(BaseModel):
#     """
#     Pydantic model for a relationship request.
#     """

#     person1: str
#     person2: str
#     strength: float


# @app.post("/relationships/add/single")
# async def add_single_relationship(relationship: RelationshipCreation):
#     try:
#         santa.add_relationship(
#             relationship.person1, relationship.person2, relationship.strength
#         )
#         return {
#             "message": "Relationship added successfully",
#             "person1": relationship.person1,
#             "person2": relationship.person2,
#             "strength": relationship.strength,
#         }
#     except Exception as e:
#         print(f"Error adding relationship: {e}")
#         return {
#             "message": "Failed to add relationship",
#             "error": str(e),
#         }


# @app.post("/relationships/add/batch")
# async def add_relationships(relationship_data: List[dict]):
#     """
#     Add multiple relationships in a single request.

#     Args:
#         relationship_data: A list of JSON objects, each containing the "person1", "person2", and "strength" keys.
#       [
#           {
#               "person1": "Alice",
#               "person2": "Bob",
#               "strength": 0.8
#           },
#           {
#               "person1": "Bob",
#               "person2": "Charlie",
#               "strength": 0.7
#           },
#           {
#               "person1": "Charlie",
#               "person2": "Alice",
#               "strength": 0.6
#           },
#           // ... additional relationships
#       ]

#     Returns:
#         A JSON object with a message and a list of successful and unsuccessful relationship additions.

#     Raises: ValueError: If the number of relationships exceeds the limit or the data is invalid.
#     """

#     if len(relationship_data) > 100:
#         raise ValueError("Maximum of 100 relationships allowed in a single request.")

#     successful_additions = []
#     failed_additions = []

#     for relationship in relationship_data:
#         try:
#             person1 = relationship["person1"]
#             person2 = relationship["person2"]
#             strength = relationship["strength"]
#             santa.add_relationship(person1, person2, strength)
#             successful_additions.append(
#                 {
#                     "person1": person1,
#                     "person2": person2,
#                     "strength": strength,
#                 }
#             )
#         except Exception as e:
#             failed_additions.append(
#                 {
#                     "message": str(e),
#                     "person1": person1,
#                     "person2": person2,
#                 }
#             )

#     return {
#         "message": "Relationships added successfully.",
#         "successful_additions": successful_additions,
#         "failed_additions": failed_additions,
#     }


"""
Typecasting via hints happen at decorated function

"""
