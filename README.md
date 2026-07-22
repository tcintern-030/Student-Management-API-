# Student Management API

A simple **Student Management API** built with **FastAPI**. This project demonstrates the fundamentals of REST API development, including routing, path parameters, request validation using Pydantic, and handling HTTP requests.

## Features

- View all students
- Get a student by ID
- Add a new student
- Request validation using Pydantic
- Interactive API documentation with Swagger UI

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn

## Project Structure

```
Student-Management-API/
│
├── __pycache__/
├── main.py
├── students.py
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone <your-repository-url>
cd Student-Management-API
```

2. Install the required packages:

```bash
pip install fastapi uvicorn
```

## Run the Application

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

The server will run at:

```
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically generates interactive API documentation.

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/students` | Get all students |
| GET | `/students/{student_id}` | Get a student by ID |
| POST | `/students` | Add a new student |

## Example Request

**POST** `/students`

```json
{
    "id": 3,
    "name": "Sara",
    "age": 22,
    "course": "Artificial Intelligence"
}
```

## Learning Objectives

This project helped me learn:

- Setting up a FastAPI application
- Creating API routes
- Using path parameters
- Working with request models
- Validating data using Pydantic
- Testing APIs with Swagger UI

## Author

**Ahmad Mustafa**

---

*This project was created for learning FastAPI and REST API development.*