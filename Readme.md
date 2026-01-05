# 🗂️ Task Management System

A **full-stack Task Management Application** built using **Django REST Framework (DRF)** for the backend and **React.js** for the frontend.  
The system allows users to **create projects, manage tasks, assign users, track progress**, and securely interact with the platform using **JWT authentication**.

---

## 🚀 Features

### 🔐 Authentication & Authorization
- User registration and login
- JWT-based authentication
- Secure API access using access & refresh tokens
- Role-based permissions

### 📁 Project Management
- Create, update, delete projects
- Assign users to projects
- View all projects with filtering & pagination

### ✅ Task Management
- Create tasks within projects
- Assign tasks to users
- Update task status (To-Do, In-Progress, Completed)
- Nested task routes under projects

### ⚙️ Backend
- Django REST Framework
- Modular & scalable architecture
- Custom permissions
- Pagination & filtering

### 🎨 Frontend
- React.js (Vite)
- Component-based UI
- State management (Redux/Context)
- Axios for API communication

---

## 🏗️ Tech Stack

### Backend
- Python
- Django
- Django REST Framework
- SimpleJWT
- SQLite (development)
- PostgreSQL (production)

### Frontend
- React.js
- Vite
- Axios
- Redux / Context API

---

## 📂 Project Structure
Task_management/
├── backend/
│   ├── task_manager/              # Django app
│   │   ├── models.py              # Database models
│   │   ├── serializers.py         # API serializers
│   │   ├── views.py               # API views
│   │   ├── urls.py                # API routes
│   │   └── permissions.py         # Custom permissions
│   ├── task_management/           # Django project config
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── manage.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/            # Reusable UI components
│   │   ├── pages/                 # Page-level components
│   │   ├── redux/                 # State management
│   │   ├── services/              # API services
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
│
└── README.md


---

## 🔄 Application Flow

User (Browser)
   ↓
React Frontend
   ↓ (Axios + JWT)
Django REST API
   ↓
Database (SQLite / PostgreSQL)

---

## ⚙️ Installation & Setup

### 📌 Backend Setup

```bash
cd backend
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Backend will be available at:
http://127.0.0.1:8000/

🔑 Authentication (JWT)

All protected routes require a JWT token.

Login Response Example
{
  "access": "<access_token>",
  "refresh": "<refresh_token>"
}

Authorization Header
Authorization: Bearer <access_token>

-----

## 📡 API Endpoints (Sample)

Authentication
POST /auth/register/
POST /auth/login/
POST /auth/token/refresh/

### Projects

GET    /projects/
POST   /projects/
PATCH  /projects/{id}/
DELETE /projects/{id}/

### Tasks

GET    /projects/{id}/tasks/
POST   /projects/{id}/tasks/
PATCH  /tasks/{id}/
DELETE /tasks/{id}/
