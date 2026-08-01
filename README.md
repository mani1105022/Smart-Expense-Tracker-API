# Smart Expense Tracker API

A REST API for managing personal expenses, built with FastAPI and Python.

## Features
- **Add an expense**: Record a new expense with title, amount, category, and date.
- **View all expenses**: Retrieve a list of all your expenses.
- **Filter expenses**: View expenses for a specific category.
- **Calculate totals**: Get the total amount spent, optionally filtered by category.
- **Delete an expense**: Remove an expense by its ID.
- **Interactive Documentation**: Available out of the box via Swagger UI (OpenAPI).

## Prerequisites
- Python 3.8+ 

## Installation

1. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Server

Start the API server using uvicorn:
```bash
uvicorn src.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.
You can view the interactive API documentation (Swagger UI) at `http://127.0.0.1:8000/docs`.

## Running Tests

To run the automated test suite, use pytest:
```bash
pytest tests/
```
