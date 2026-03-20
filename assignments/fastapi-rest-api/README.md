# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and implement RESTful APIs using the FastAPI framework in Python. You will practice creating endpoints, handling requests and responses, and working with data models.

## 📝 Tasks

### 🛠️ Create a Simple FastAPI Application

#### Description
Set up a basic FastAPI project and create your first API endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Install and import FastAPI
- Create an instance of the FastAPI app
- Implement a root endpoint (`/`) that returns a JSON welcome message
- Run the application locally


### 🛠️ Implement CRUD Operations for a Resource

#### Description
Add endpoints to perform Create, Read, Update, and Delete (CRUD) operations for a simple resource, such as a list of books.

#### Requirements
Completed program should:

- Define a Pydantic model for the resource (e.g., Book)
- Implement endpoints for:
  - Creating a new resource (POST)
  - Reading all resources (GET)
  - Reading a single resource by ID (GET)
  - Updating a resource by ID (PUT)
  - Deleting a resource by ID (DELETE)
- Use in-memory storage (a Python list) for the resource data
- Return appropriate status codes and messages for each operation

### 🛠️ Add Input Validation and Error Handling

#### Description
Enhance your API with input validation and custom error handling.

#### Requirements
Completed program should:

- Validate incoming data using Pydantic models
- Return helpful error messages for invalid input
- Handle 404 errors for missing resources
