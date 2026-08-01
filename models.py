from pydantic import BaseModel, Field
from datetime import date
import uuid

class ExpenseCreate(BaseModel):
    title: str = Field(...)
    amount: float = Field(..., gt=0)
    category: str = Field(...)
    date: date

class Expense(ExpenseCreate):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
