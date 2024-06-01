# Hydroponic System Management

This project is a simple CRUD application built with Django and Django REST Framework for managing hydroponic systems. Users can create, read, update, and delete information about their hydroponic systems and associated measurements.

## Features

- User registration and authentication with JWT.
- CRUD operations for hydroponic systems.
- CRUD operations for measurements.
- Filtering, sorting, and pagination for data retrieval.

## Installation

### Prerequisites

- Python 3.6+
- Django 3.0+
- PostgreSQL (or any other preferred database)

### Steps

1. **Clone the repository:**

```bash
    git clone https://github.com/Kaldinn/HydroponicTask.git
    cd hydroponic_system
```

2. **Create Virtual environment:**

```bash
    python -m venv venv
    source venv/Scripts/activate 
```

3. **Install the required packages:**

```bash
    pip install -r requirements.txt
```

4. **Apply the migrations:**

```bash
    python manage.py migrate
```

5. **Create superuser:**

```bash
    python manage.py createsuperuser
```

6. **Run the development server:**

```bash
    python manage.py runserver
```
