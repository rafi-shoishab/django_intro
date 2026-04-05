# Django Intro - 🚀

This project demonstrates the basic workflow of Django:

* Django project setup ✔ - Django install, Create project, runserver, Project structure, startapp, settings.py
* URL Routing ✔ - urls.py, path(), include(), project urls vs app urls
* Views ✔ - function based views, HttpResponse, render(), redirect()
* Templates ✔ - template folder, variables, loops, conditions, template inheritance, include
* Static Files ✔ - static folder, STATIC_URL, {% load static %}
* Models (Database) ✔ - models.py, field types, relationships, makemigrations, migrate
* CRUD Operations ✔ - 
            Create → create data
            Read → list view
            Update → edit data
            Delete → remove data
  
* Forms ✔ - Django forms, ModelForm, validation
* File & Image Upload ✔ - ImageField, MEDIA_ROOT, MEDIA_URL
* Security ✔ - CSRF, authentication, permissions, XSS protection, SQL injection protection
* Search & Filtering ✔ - Database search, Query search, icontains, Filter results 
* Authentication (Auth) ✔ - register, login, logout, authenticate(), login_required decorator
* Custom User Model ✔ - AbstractUser, AbstractBaseUser, Custom fields, Role based system
* Permissions & Groups - Access control, user roles, group permissions, decorators
* Pagination - Large data handle
* Signals - Automatic events
            user create → profile auto create
* Middleware - Custom request processing, Authentication, Logging
* Caching - Redis, Memcached
* Django REST Backend API - Django REST Framework (DRF), serializers, API views, Token Auth, O Auth, JWT auth, ViewSets, Routers
* Serializers - Convert models to JSON 
* Deployment Project live - Gunicorn, Nginx, Docker, PostgreSQL, VPS
* Scaling & Production - Load balancing, Cloud hosting, Monitoring, CI/CD

This is a beginner-friendly project to understand how Django works internally.

---

## 📌 Project Overview

This project shows how:

* Django handles HTTP requests
* Views return responses
* URLs connect to views
* Templates render HTML pages

---

## 🏗 Project Structure

```
django-intro-template/
│
├── core/                   # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── navigation/             # Django app
│   ├── views.py
│   ├── urls.py
│   └── models.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── manage.py
└── requirements.txt
```

---

## ⚡ 1. Setup Django (Run Project)

### 1.0 Clone Repository

```
git clone https://github.com/rafi-shoishab/django-intro.git
cd django-intro
```

---

### 1.1 Create Virtual Environment

Mac/Linux

```
python3 -m venv .venv
source .venv/bin/activate
```

Windows

```
python -m venv .venv
.venv\Scripts\activate
```

---

1.2 Install Dependencies

```
pip install -r requirements.txt
pip install django
pip install pillow
```

---

1.3 Run Development Server

```
python manage.py runserver
```

1.4 Open browser:

```
http://127.0.0.1:8000
```

---

## 🌐 2. HTTP Response Implementation

This section explains how to return a simple HTTP response in Django.

---

### Step 2.0 — Create Django Project

```
django-admin startproject core 
```

---

---

### Step 2.1 — Create Django App

```
python manage.py startapp navigation
```

---

### Step 2.2 — Register App in settings.py

File: `core/settings.py`

Add the app inside `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'navigation',
]
```

---

### Step 2.3 — Create View (HTTP Response)

File: `navigation/views.py`

```python
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello Django")
```

This view returns a simple text response.

---

### Step 2.4 — Create App URL Configuration

Create file: `navigation/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
]
```

---

### Step 2.5 — Connect App URLs to Project URLs

File: `core/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('navigation.urls')),
]
```

---

### Test HTTP Response

Run server and visit:

```
http://127.0.0.1:8000/hello/
```

You will see:

```
Hello Django
```

---

## 🎨 3. Template Rendering Implementation

This section explains how Django renders HTML templates.

---

### Step 3.1 — Create Templates Folder

Create folder structure:

```
templates/index.html
```

---

### Step 3.2 — Configure Template Directory in settings.py

File: `core/settings.py`

Update the `TEMPLATES` section:

```python
import os

TEMPLATES = [
{
...
'DIRS': [os.path.join(BASE_DIR, 'templates')],
... 
}
]
```

This tells Django where to find HTML templates.

---

### Step 3.3 — Create HTML Template

File: `templates/index.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Django Home</title>
</head>
<body>
    <h1>Hello Django Template 🎉</h1>
</body>
</html>
```

---

### Step 3.4 — Create View to Render Template

File: `navigation/views.py`

```python
from django.shortcuts import render

def home(request):
    return render(request, "index.html")
```

---

### Step 3.5 — Add URL Route

File: `navigation/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

---

### Step 3.6 - Test Template Rendering

Run server and visit:

```
http://127.0.0.1:8000/
```

The HTML page will render.

---

## 🔁 Django Request → Response Flow

```
User Request
     ↓
URL Routing (urls.py)
     ↓
View Function (views.py)
     ↓
Template Rendering
     ↓
HTTP Response
```

---

## 🎯 Learning Objectives

This project helps you learn:

* Django project setup
* Creating Django apps
* URL routing
* HTTP response handling
* Template rendering
* Django request lifecycle

---

## 🔧 Git Workflow (Quick Guide)

### First Time Setup

```
git init
git add .
git commit -m "initial commit"
git remote add origin https://github.com/rafi-shoishab/django-intro-template.git
git branch -M main
git push -u origin main
```

---

### Daily Development Workflow (always follow)

```
git pull
git add .
git commit -m "update message"
git push
```

---

### Recommended `.gitignore`

```
.venv/
venv/
__pycache__/
*.pyc
db.sqlite3
.DS_Store
.vscode/
```

---

### 👨‍💻 Author

Rafiur Rahman Shoishab
GitHub: https://github.com/rafi-shoishab

---

# 📄 License

This project is created for educational purposes.




