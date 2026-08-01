from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from .models import Expense, ExpenseCreate
import uuid

app = FastAPI(
    title="Smart Expense Tracker API",
    description="API to manage personal expenses",
    version="1.0.0"
)

# In-memory storage for expenses
expenses_db: List[Expense] = []

@app.post("/expenses", response_model=Expense, status_code=201)
def add_expense(expense_in: ExpenseCreate):
    new_expense = Expense(
        id=str(uuid.uuid4()),
        title=expense_in.title,
        amount=expense_in.amount,
        category=expense_in.category,
        date=expense_in.date
    )
    expenses_db.append(new_expense)
    return new_expense

@app.get("/expenses", response_model=List[Expense])
def get_expenses(category: Optional[str] = Query(None, description="Filter by category")):
    if category:
        filtered = [exp for exp in expenses_db if exp.category.lower() == category.lower()]
        return filtered
    return expenses_db

@app.get("/expenses/total")
def get_total_expenses(category: Optional[str] = Query(None, description="Filter by category")):
    if category:
        total = sum(exp.amount for exp in expenses_db if exp.category.lower() == category.lower())
    else:
        total = sum(exp.amount for exp in expenses_db)
    return {"total": total}

@app.delete("/expenses/{expense_id}", status_code=204)
def delete_expense(expense_id: str):
    for i, exp in enumerate(expenses_db):
        if exp.id == expense_id:
            del expenses_db[i]
            return
    raise HTTPException(status_code=404, detail="Expense not found")
