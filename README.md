# eskejob Backend API

A RESTful backend API for a job recruitment platform where companies can post jobs and applicants can apply.
Built with Django, Django REST Framework, JWT authentication, and MinIO for media storage.
Implements role-based access control, ownership enforcement, file uploads, pagination, and search.

---

## Features
- **User Roles**: `applicant` and `company`
- **Authentication**: JWT-based login & registration with email verification
- **Job Management**: Companies can create, update, delete, and view their job posts
- **Applications**: Applicants can apply to jobs, upload resumes, and track application statuses
- **Search & Pagination**: Jobs and applications with filters and sorting
- **File Uploads**: Resume upload with format validation (`.pdf`, `.docx`)
- **Swagger & ReDoc** API documentation

---

## Technology Choices
- **Django** – Powerful and mature Python web framework
- **Django REST Framework (DRF)** – Flexible toolkit for building APIs
- **JWT Authentication** – Secure token-based authentication
- **MinIO** – Object storage for media files (e.g., resumes)
- **Docker** – Containerized development and deployment
- **Swagger / ReDoc** – Auto-generated API documentation

---

## Setup & Installation

### 1 Clone Repository
```bash
git clone https://github.com/yourusername/eskalate-backend.git
cd eskalate-backend
````

### 2️ Create Environment Variables

Copy `.env.example` to `.env` and configure your environment variables.

```bash
cp .env.example .env
```

#### Option A – Using pip

```bash
pip install -r requirements.txt
```

#### Option B – Using uv

```bash
uv sync
```

---

## Running the Project Locally

### Run Migrations

```bash
python manage.py migrate
```

### Start Development Server

#### Option A – Using Docker

```bash
docker compose up --build
```

#### Option B – Using `runserver`

```bash
python manage.py runserver
```

---

##  API Documentation

* **Swagger UI**: [http://localhost:8000/doc/](http://localhost:8000/doc/)
* **ReDoc**: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

---

## Non-Functional Requirements Implemented

### 1. **Security**

* JWT authentication with strong password hashing (PBKDF2)
* Role-based access control
* Email verification before account activation
* File type validation for resume uploads

### 2. **Performance & Scalability**

* Pagination & filtering to optimize queries
* Docker for easy scaling

### 3. **Abuse Prevention**

* Validation to prevent duplicate applications

### 4. **Code Quality**

* Modular Django app structure
* Consistent response format
* Clean error handling

---

## Testing

TODO
