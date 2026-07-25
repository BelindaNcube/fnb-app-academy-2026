# FNB App Academy 2026 — Python Foundations

Practical work from the **FNB App Academy 2026**, a Python and app-development programme delivered by the **University of Johannesburg's Johannesburg Business School**, in partnership with **Accenture**. This repository tracks my progress through the course: every practical task and bonus challenge, unit by unit, building from first-principles Python toward a full mobile app built in Kivy.

I'm building this alongside my day job as a **Credit Analyst** in business banking, where I assess credit risk on business overdraft facilities. That real-world context shapes a lot of the design choices here — several exercises and my planned capstone project are directly inspired by problems I solve at work every day.

---

## About the Programme

The FNB App Academy is a structured, part-time programme covering:

- Python fundamentals (strings, numbers, data structures, control flow)
- Object-oriented programming, file handling, and error management
- Mobile app development with Kivy
- Connecting apps to real-world data via APIs
- A final capstone build and presentation

Full programme details: [academy.appoftheyear.co.za](https://academy.appoftheyear.co.za/)

---

## Repository Structure

Each unit has its own folder, containing the main practical task and the bonus challenge for that unit:

```
fnb-app-academy-2026/
├── unit1/    Introduction to Python
├── unit2/    String Manipulation and Formatting
├── unit3/    Arithmetic Operations and Type Casting
├── unit4/    Conditional Logic and Decision-Making
├── unit5/    Data Structures (Lists and Dictionaries)
├── unit6/    Loops and Iteration
├── ...
├── .gitignore
└── README.md
```

More units will be added here as the course progresses through Object-Oriented Programming, File Handling, Kivy, and API integration.

---

## Units Completed So Far

### Unit 1 — Introduction to Python
First steps into Python: variables, data types (`str`, `int`, `float`, `bool`), `input()`/`print()`, and `type()` inspection.
- **`student_info.py`** — collects a user's details and displays a formatted profile card, demonstrating all four core data types, string casing methods, and arithmetic.
- **`concert_ticket_booker.py`** — a simple, friendly booking confirmation script using f-strings.

### Unit 2 — String Manipulation and Formatting
Working with text: string methods, indexing and slicing, and clean formatted output.
- **`string_formatter.py`** — builds a username from a user's name, cleans and analyses a bio message using `.strip()`, `.replace()`, and `len()`.
- **`password_hint_tool.py`** — generates a secure password hint using first/last character indexing (including negative indexing).

### Unit 3 — Arithmetic Operations and Type Casting
Python's arithmetic operators, and the importance of converting between data types.
- **`calculator.py`** — a multi-function calculator covering all four basic operations plus floor division and modulus, safely guarded against division by zero, with results displayed in a clean formatted table.
- **`fuel_cost_calculator.py`** — calculates estimated petrol costs for a road trip based on distance and fuel price per litre — a small, practical tool relevant to South African drivers.

### Unit 4 — Conditional Logic and Decision-Making
`if`/`elif`/`else` chains, comparison and logical operators, and why condition order matters.
- **`grade_classifier.py`** — takes a learner's marks across three subjects and produces a full report card: average, letter grade, pass/fail status, and intervention flags for weak subjects.
- **`atm_withdrawal_simulator.py`** — simulates a bank withdrawal, correctly validating for invalid (zero/negative) amounts before checking sufficient funds — a small but important lesson in condition ordering.

### Unit 5 — Data Structures: Lists and Dictionaries
Organising and managing collections of data, and understanding mutability.
- **`contact_book.py`** — a full command-line contact manager storing contacts as a list of dictionaries, with add, search, delete, and view functions behind a menu-driven interface.
- **`phone_directory_search.py`** — a compact phone lookup using a dictionary, with a note on why phone numbers are stored as strings (to preserve leading zeros).

### Unit 6 — Loops and Iteration
`for` and `while` loops, `range()`, `break`/`continue`, and combining loops with conditionals.
- **`grade_report.py`** — extends the Unit 4/5 grade logic into a full class report: processes multiple students, calculates class-wide statistics (average, highest, lowest), and includes an interactive student lookup.
- **`high_score_tracker.py`** — a continuous game-score loop demonstrating safe input handling and the `break` keyword.

*(More units to be added as the course continues.)*

---

## Tech Stack

- **Language:** Python 3.13
- **IDE:** PyCharm
- **Version control:** Git & GitHub

---

## What's Next

The next phase of this repository will introduce:
- Object-oriented programming, file handling, and error management
- A Kivy-based mobile UI
- Multi-screen app development
- API integration for live data

The course culminates in a capstone project. Mine will be a **Facility Health Dashboard** — a customer-facing concept prototype (built with entirely fictional data) that shows business overdraft holders their facility's health status in plain language, helping them understand what's needed to avoid a limit reduction plan before it happens. Alongside it, I'm separately building an internal analyst-facing companion tool, **Facility Watch**, to explore how reduction-plan monitoring could be dashboarded for my own team.

---

## About Me

Credit Analyst by day, learning to build apps by night. Connect with me on [LinkedIn](https://www.linkedin.com/in/belinda-ncube) if you'd like to follow the journey.
