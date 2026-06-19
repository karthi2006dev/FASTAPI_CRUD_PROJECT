# FASTAPI CRUD PROJECT

A robust RESTful CRUD API built using **FastAPI**, **SQLAlchemy ORM**, and **PostgreSQL** to manage and generate student marksheets.

## 🚀 Features
* **Full CRUD Operations**: Create, Read, Update, and Delete student detail profiles.
* **Data Validation**: Enforced strict request/response schemas using **Pydantic v2** (`from_attributes`).
* **Database Management**: Automated table creation and session handling via **SQLAlchemy** connected to PostgreSQL.
* **Environment Security**: Sensitive database connections managed securely via `.env` files.

---

## 🛠️ Tech Stack
* **Framework**: FastAPI
* **Database**: PostgreSQL
* **ORM**: SQLAlchemy
* **Validation**: Pydantic
* **Server**: Uvicorn

---

## 💻 Local Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/api_crud_project.git](https://github.com/YOUR_USERNAME/api_crud_project.git)
   cd api_crud_project

## GUIDE
**step 1:**
Navigate into the project directory:
```bash
cd api_crud_project
```
**Step 2: Set up a virtual environment**
```bash
python -m venv .venv
```
# On Windows (PowerShell):
```bash
.venv\Scripts\activate
```
# On Mac/Linux:
source .venv/bin/activate

