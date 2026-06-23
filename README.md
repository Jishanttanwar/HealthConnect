# 🏥 HealthConnect Backend

A scalable Healthcare Management Platform built using Django REST Framework (DRF). HealthConnect provides secure APIs for managing patients, doctors, appointments, medical records, prescriptions, lab reports, and healthcare workflows.

---

## 🚀 Features

### Authentication & Authorization
- Custom User Model
- JWT Authentication
- Role-Based Access Control (RBAC)
- Email-based Login
- Protected APIs

### User Roles
- Patient
- Doctor
- Receptionist
- Admin

### Healthcare Modules
- Patient Management
- Doctor Management
- Departments
- Specializations
- Doctor Availability
- Appointment Scheduling
- Clinical Encounters
- Medical Records
- Prescriptions
- Lab Reports
- Notifications
- Audit Logs

---

## 🏗️ Project Architecture

```text
HealthConnect/
│
├── accounts/
├── patients/
├── doctors/
├── departments/
├── appointments/
├── encounters/
├── medical_records/
├── prescriptions/
├── lab_reports/
├── notifications/
├── core/
│
├── config/
├── manage.py
└── requirements.txt
```

---

## 🗄️ Database Design

The project follows a modular healthcare database architecture.

### Core Entities

```text
User
├── PatientProfile
└── DoctorProfile

DoctorProfile
├── Department
└── Specialization

Patient
    │
Appointment
    │
Encounter
    │
MedicalRecord
    │
Prescription
    │
PrescriptionItems

Patient
    │
LabReports

User
├── Notifications
└── AuditLogs
```

---

## 🛠️ Tech Stack

### Backend
- Python
- Django
- Django REST Framework

### Authentication
- JWT (SimpleJWT)

### Database
- MySQL

### API Testing
- Insomnia

### Documentation
- DRF Browsable API
- OpenAPI/Swagger (Planned)

### Version Control
- Git
- GitHub

---

## 🔐 Authentication Flow

### Register

```http
POST /api/accounts/register/
```

### Login

```http
POST /api/accounts/login/
```

### Refresh Token

```http
POST /api/accounts/refresh/
```

### Current User

```http
GET /api/accounts/me/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Jishanttanwar/HealthConnect.git
cd HealthConnect
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### macOS/Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory.

```env
SECRET_KEY=your-secret-key

DEBUG=True

DB_NAME=healthconnect
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
```

---

## 🗃️ Database Setup

Create MySQL database:

```sql
CREATE DATABASE healthconnect;
```

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create superuser:

```bash
python manage.py createsuperuser
```

---

## ▶️ Run Server

```bash
python manage.py runserver
```

Visit:

```text
http://127.0.0.1:8000/
```

Admin Panel:

```text
http://127.0.0.1:8000/admin/
```

---

## 📋 Current Progress

### Completed

- [x] Project Setup
- [x] MySQL Configuration
- [x] Custom User Model
- [x] JWT Authentication
- [x] User Registration API
- [x] Login API
- [x] Current User API
- [x] GitHub Repository Setup

### In Progress

- [ ] Departments Module
- [ ] Specializations Module
- [ ] Doctor Profiles
- [ ] Patient Profiles

### Planned

- [ ] Appointments
- [ ] Encounters
- [ ] Medical Records
- [ ] Prescriptions
- [ ] Lab Reports
- [ ] Notifications
- [ ] Audit Logs
- [ ] Swagger Documentation
- [ ] Docker Deployment

---

## 🎯 Learning Objectives

This project is being built to learn and demonstrate:

- Django Backend Development
- REST API Design
- Authentication & Authorization
- Database Design
- Healthcare Informatics Concepts
- Role-Based Access Control
- Production-Ready Backend Practices

---

## 👨‍💻 Author

**Jishant Tanwar**

- B.Tech CSE (Health Informatics)
- VIT Bhopal University
