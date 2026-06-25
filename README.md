# 💰 Expense Tracker

A full-stack personal expense management web application built with **Django** that helps users manage expenses, income, budgets, and financial insights. The project follows a clean architecture with authentication, service layers, REST APIs, and user-specific data isolation.

---

## 🚀 Features

### 👤 Authentication

* User Registration
* User Login & Logout
* Change Password
* Forgot Password (Email Reset)
* Session Authentication

---

### 💵 Expense Management

* Add Expense
* Edit Expense
* Delete Expense
* View Expense History
* Category-wise Expenses
* Date Tracking

---

### 💰 Income Management

* Add Income
* Edit Income
* Delete Income
* Income History

---

### 📊 Dashboard

* Total Income
* Total Expenses
* Savings Calculation
* Recent Expenses
* Category-wise Expense Distribution

---

### 📂 Categories

* User-specific Categories
* Custom Category Creation
* Category Isolation Between Users

---

### 🎯 Budgets

* Monthly Budget Creation
* Budget Tracking
* Overspending Detection (Rule-based)

---

### 🌐 REST APIs (Django REST Framework)

Read-only APIs implemented for:

* Expenses
* Income
* Categories
* Dashboard Summary

These APIs are protected using authentication and return only the logged-in user's data.

---

## 🏗 Project Architecture

```
Expense_Tracker/
│
├── accounts/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   └── urls.py
│
├── expenses/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── services.py
│   ├── api/
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│   └── templates/
│
├── static/
│   ├── css/
│   └── images/
│
├── templates/
│
├── config/
│
└── manage.py
```

---

## 🛠 Tech Stack

### Backend

* Django
* Django REST Framework
* Python

### Database

* SQLite (Development)

### Frontend

* HTML5
* CSS3
* Django Templates

### Authentication

* Django Authentication System
* Custom Abstract User Model

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/deepaktangudu45/Expense_tracker
```

Navigate into the project

```bash
cd ExpenseTracker
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Apply migrations

```bash
python manage.py migrate
```

Run the development server

```bash
python manage.py runserver
```

---

## 🔑 API Endpoints

| Method | Endpoint           | Description          |
| ------ | ------------------ | -------------------- |
| GET    | `/api/expenses/`   | List user expenses   |
| GET    | `/api/income/`     | List user income     |
| GET    | `/api/categories/` | List user categories |
| GET    | `/api/dashboard/`  | Dashboard summary    |

---

## 📚 Concepts Practiced

* Django Models
* Custom User Model
* ModelForms
* Class-Based Authentication
* Django ORM
* QuerySets
* Aggregation & Annotation
* Service Layer Architecture
* REST APIs
* Model Serializers
* User Authentication
* Authorization
* CRUD Operations
* Template Inheritance
* Static File Management

---

## 📈 Future Improvements

Planned features include:

* POST/PUT/DELETE REST APIs
* AI-powered Expense Categorization
* Spending Pattern Analysis
* Monthly Expense Prediction
* CSV / Excel Export
* Charts & Interactive Dashboard
* Email Notifications
* Docker Support
* Deployment on AWS / Render