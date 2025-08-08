# 🌍 Location Selector with FastAPI, MySQL & Vanilla JS

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?logo=fastapi)
![License](https://img.shields.io/badge/License-MIT-orange)
![Database](https://img.shields.io/badge/Database-MySQL-blue?logo=mysql)

A **lightweight** and **extensible** web application that dynamically loads  
**Country → State → City** selections using a FastAPI backend, MySQL database,  
and a modern HTML/CSS/JS frontend.

---

## ✨ Features

- **Dynamic cascading dropdowns** (Country → State → City).
- **FastAPI** backend serving JSON endpoints.
- **CORS enabled** for smooth frontend-backend communication.
- **SQLAlchemy ORM** for clean database models.
- **MySQL-ready** with included `.sql` files for instant setup.
- **Easy to extend** for small handy features.

---

## 📂 Project Structure

.
├── app/
│ ├── main.py # FastAPI app & API routes
│ ├── models.py # SQLAlchemy ORM models
│ ├── db.py # Database connection setup
│
├── templates/
│ └── index.html # Frontend HTML/CSS/JS
│
├── sql/
│ ├── countries.sql # Initial countries data
│ ├── states.sql # Initial states data
│ └── cities.sql # Initial cities data
│
└── README.md




---

## 🛠 Tech Stack

**Frontend:** HTML, CSS, JavaScript (Vanilla)  
**Backend:** Python 3.x, FastAPI, SQLAlchemy  
**Database:** MySQL (mysql-connector-python driver)  
**Others:** Jinja2 Templates, CORS Middleware

---
## ⚡ Quick Start

### 1️⃣ Clone the Repository
Clone the repository from GitHub:
```bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo

2️⃣ Create & Activate Virtual Environment
Ubuntu/MacOS:
bash

python3 -m venv venv
source venv/bin/activate


Windows (PowerShell):

powershell
python -m venv venv
venv\Scripts\activate



3️⃣ Install Dependencies
If a requirements.txt file exists:

bash

pip install -r requirements.txt
Or install manually:

bash

pip install fastapi uvicorn sqlalchemy mysql-connector-python jinja2


🚀 Running the Application
From the project root:
bash
uvicorn app.main:app --reload