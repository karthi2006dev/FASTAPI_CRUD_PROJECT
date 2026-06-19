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
**Step 1:Navigate into the project directory**
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
```bash
source .venv/bin/activate
```
**Step 3:Install required dependencies**
```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv
```
**Step 4: Configure Environment Variables (.env)**
Create a file named .env in the root folder of your project. You must use your actual local PostgreSQL administrative username and password to create the connection string.

Add this line to your .env file:DATABASE_URL=postgresql://<YOUR_POSTGRES_USER>:<YOUR_POSTGRES_PASSWORD>@localhost:5432/<YOUR_DATABASE_NAME>

**Step 5: Start the FastAPI Server**
With your virtual environment active, run the server using Uvicorn:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```
**Step 6: Test the API Using Postman**
Open Postman to send requests directly to your running FastAPI server and verify the CRUD operations:
create get post delete update requests using the endpoints
and test the api.
