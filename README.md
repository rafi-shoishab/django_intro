# Django Intro Template 🚀

This project demonstrates the basic workflow of Django:

* Django project setup
* HTTP response handling
* URL routing
* Template rendering (HTML)
* Django request → response flow

This is a beginner-friendly project to understand how Django works internally.

---

# 📌 Project Overview

This project shows how:

* Django handles HTTP requests
* Views return responses
* URLs connect to views
* Templates render HTML pages

---

# 🏗 Project Structure

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

# ⚡ 1. Setup Django (Run Project)

## Clone Repository

```
git clone https://github.com/rafi-shoishab/django-intro-template.git
cd django-intro-template
```

---

## Create Virtual Environment

### Mac/Linux

```
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```
python -m venv .venv
.venv\Scripts\activate
```

---

## Install Dependencies

```
pip install -r requirements.txt
```

---

## Run Development Server

```
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000
```

---

# 🌐 2. HTTP Response Implementation

This section explains how to return a simple HTTP response in Django.

---

## Step 1 — Create Django App

```
python manage.py startapp navigation
```

---

## Step 2 — Register App in settings.py

File: `core/settings.py`

Add the app inside `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'navigation',
]
```

---

## Step 3 — Create View (HTTP Response)

File: `navigation/views.py`

```python
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello Django")
```

This view returns a simple text response.

---

## Step 4 — Create App URL Configuration

Create file: `navigation/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
]
```

---

## Step 5 — Connect App URLs to Project URLs

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

## Test HTTP Response

Run server and visit:

```
http://127.0.0.1:8000/hello/
```

You will see:

```
Hello Django
```

---

# 🎨 3. Template Rendering Implementation

This section explains how Django renders HTML templates.

---

## Step 1 — Create Templates Folder

Create folder structure:

```
templates/index.html
```

---

## Step 2 — Configure Template Directory in settings.py

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

## Step 3 — Create HTML Template

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

## Step 4 — Create View to Render Template

File: `navigation/views.py`

```python
from django.shortcuts import render

def home(request):
    return render(request, "index.html")
```

---

## Step 5 — Add URL Route

File: `navigation/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

---

## Test Template Rendering

Run server and visit:

```
http://127.0.0.1:8000/
```

The HTML page will render.

---

# 🔁 Django Request → Response Flow

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

# 🎯 Learning Objectives

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

# 👨‍💻 Author

Rafiur Rahman Shoishab
GitHub: https://github.com/rafi-shoishab

---

# 📄 License

This project is created for educational purposes.
