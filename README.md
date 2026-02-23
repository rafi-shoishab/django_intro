# Django Intro Template 🚀

This project demonstrates the basic workflow of Django:

* Django project setup
* HTTP response handling
* URL routing
* Template rendering (HTML)
* Django request → response flow

This is a beginner-friendly project to understand how Django works internally.

---

# 🎯 Learning Objectives

This project helps you learn:

* Django project setup
* Creating Django apps
* URL routing
* HTTP response handling
* Template rendering
* django default admin panal exploration
* Django request lifecycle

---

## 🏗 Project Structure Overview

django-intro-template-admin/
│
├── core/ # Django project configuration
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── navigation/ # Django app
│ ├── models.py # Database models
│ ├── admin.py # Admin panel configuration
│ ├── views.py
│ └── urls.py
│
├── db.sqlite3 # SQLite database
├── manage.py
└── requirements.txt


---

# 📌 Project Overview

This project shows how:

* Django handles HTTP requests
* Views return responses
* URLs connect to views
* Templates render HTML pages

---

# ⚡ 1. Setup Django (Run Project)

## Clone Repository

```
git clone https://github.com/rafi-shoishab/django-intro-template-admin-media.git 
cd django-intro-template-admin-media
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

✅ This section explains how to return a simple HTTP response in Django.

---

## Step 0.1 — Create Django App

```
python manage.py startapp navigation
```

---

## Step 0.2 — Register App in settings.py

File: `core/settings.py`

Add the app inside `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'navigation',
]
```

---

## Step 0.3 — Create View (HTTP Response)

File: `navigation/views.py`

```python
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello Django")
```

✅ This view returns a simple text response.

---

## Step 0.4 — Create App URL Configuration

Create file: `navigation/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
]
```

---

## Step 0.5 — Connect App URLs to Project URLs

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

✅ This section explains how Django renders HTML templates.

---

## Step 1.1 — Create Templates Folder

Create folder structure:

```
templates/index.html
```

---

## Step 1.2 — Configure Template Directory in settings.py

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

✅ This tells Django where to find HTML templates.

---

## Step 1.3 — Create HTML Template

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

## Step 1.4 — Create View to Render Template

File: `navigation/views.py`

```python
from django.shortcuts import render

def home(request):
    return render(request, "index.html")
```

---

## Step 1.5 — Add URL Route

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

# 🛠 Django Admin Panel Exploration

Django Admin Panel is a built-in feature that allows developers and administrators
to manage database records visually without writing SQL queries.

---
# ⚙️ Step 3.1 — Apply Database Migrations

Django admin requires some default database tables (users, permissions, sessions).

Run:

python manage.py migrate


✅ Creates database tables

✅ Prepares the admin panel backend

✅ Updates db.sqlite3

---

# ⚙️ Step 3.2: Create a Superuser (Admin Account)

To access the admin panel, you must create a superuser:

python manage.py createsuperuser

You will be asked for:

Username

Email (optional)

Password

Confirm Password

✅ This user will have full admin access.

---

# ⚙️ Step 3.3: Create a Model

Models define the structure of database tables.

📄 File: navigation/models.py

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField(unique=True)
    department = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

✅ This model represents a Student table in the database.

---

# ⚙️ Step 3.4: Create Model Migrations

After creating or updating a model, run:

python manage.py makemigrations
python manage.py migrate

✅ Convert models into database tables (makemigrations)

✅ Apply changes to the database (migrate)

---

# ⚙️ Step 3.5: Register Model in Admin Panel

Models do not appear in the admin panel automatically.

📄 File: navigation/admin.py

from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll', 'department', 'created_at')
    search_fields = ('name', 'roll')
    list_filter = ('department',)

Explanation:

✅ list_display → Shows fields as columns

✅ search_fields → Adds a search box

✅ list_filter → Adds filter sidebar

---

# ⚙️ Step 3.6: Run Development Server

python manage.py runserver

Access Django Admin Panel

Open your browser and visit:

http://127.0.0.1:8000/admin/

---

# 🗄 Database Exploration

Default database: SQLite

File location: db.sqlite3

All admin panel actions directly modify the database

You can view data using:

Django Admin Panel

SQLite DB Browser

# 🔐 Users & Permissions

Using the admin panel, you can:

Create staff users

Assign permissions

Control access to models

Manage user roles securely

---

## ⚙️ Step 3.7: Create Model with variety of field

📄 **File:** `navigation/models.py`

from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=100)
    std_id = models.IntegerField(unique=True)
    age = models.IntegerField()
    email = models.EmailField(max_length=100, unique=True)
    dob = models.DateField()
    dept = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    image = models.ImageField(upload_to='student_img/', null=True, blank=True)

    def __str__(self):
        return self.name

✅ ImageField allows uploading student profile images.
✅ upload_to='student_img/' → Uploaded images are saved inside MEDIA_ROOT/student_img/.

---

# ⚙️ Step 3.8: Register Model Using Decorator

📄 File: navigation/admin.py

from django.contrib import admin
from .models import Students

# Using @admin.register decorator
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'std_id', 'age', 'email', 'dob', 'dept')
    search_fields = ('name', 'std_id', 'email')
    list_filter = ('dept',)
    ordering = ('id',)

Explanation:

✅ @admin.register(Students) → Registers the Students model directly

✅ list_display → Columns visible in admin table

✅ search_fields → Adds search bar for listed fields

✅ list_filter → Adds filter sidebar for quick filtering

✅ ordering → Default sort order in admin

✅ Using decorator is cleaner than admin.site.register(Students, StudentsAdmin)

---

# ⚙️ Step 3.9: Configure Media Settings

📄 File: core/settings.py

Add:

import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

✅ MEDIA_URL → URL path to access media in browser

✅ MEDIA_ROOT → Physical path to store uploaded files

---

# ⚙️ Step 3.10: Serve Media Files in Development

📄 File: core/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('navigation.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

✅ This allows Django development server to serve uploaded files.

---

## 🔧 Git Workflow (Quick Guide)

### First Time Setup

```
git status
git add .
git commit -m "initial commit"
git remote add origin https://github.com/rafi-shoishab/django-intro-template-media.git
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
