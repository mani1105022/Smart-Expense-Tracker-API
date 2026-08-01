# AI Notes

1. **Which parts of the code were AI-generated vs. written by you**
   I used ChatGPT to generate the initial boilerplate for the FastAPI app (setting up the `FastAPI()` instance and standard imports) and the basic Pydantic model structure in `src/models.py`. The actual endpoint logic, routing, and filtering logic were written and tweaked by me to match the exact requirements of the assignment.

2. **What you validated, tested, or changed in the AI's output, and why**
   The AI initially suggested using SQLite with SQLAlchemy, but I changed it to use a simple in-memory list (`expenses_db`) because the assignment stated "no database is required" and I wanted to keep the project lightweight and simple. I also manually wrote and validated the pytest suite (`test_main.py`) to ensure all the edge cases for calculating totals and deleting items were covered properly.

3. **Any AI suggestion you decided not to use, and why**
   The AI suggested creating a separate `routers/` directory to modularize the application. While that's a great practice for larger apps, I decided not to use it here. Given that there are only a handful of endpoints and the time constraint, keeping everything in `main.py` is cleaner and easier to read for this specific exercise.
