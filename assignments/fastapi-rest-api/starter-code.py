# Starter Code for FastAPI REST API Assignment

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Define your data model here
# class Book(BaseModel):
#     ...

# In-memory storage for books
books = []

# TODO: Implement root endpoint
# @app.get("/")
# async def root():
#     ...

# TODO: Implement CRUD endpoints for Book resource
# @app.post("/books")
# async def create_book(...):
#     ...

# @app.get("/books")
# async def get_books():
#     ...

# @app.get("/books/{book_id}")
# async def get_book(book_id: int):
#     ...

# @app.put("/books/{book_id}")
# async def update_book(book_id: int, ...):
#     ...

# @app.delete("/books/{book_id}")
# async def delete_book(book_id: int):
#     ...
