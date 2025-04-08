# 📝 SimpleWeblog

SimpleWeblog is a basic blogging platform built with Django.  
It allows users to create, read, update, and delete blog posts through a simple and clean interface.

---

## 🚀 Features

- View a list of all posts
- View individual post details
- Admin panel for managing content

---

## 📦 Requirements

- Python 3.10+
- Django 5.x or higher
- (Optional) Virtualenv

---

## ⚙️ Installation

### 1. Clone the project

```bash
git clone https://github.com/Esmat434/SimpleWeblog.git
cd SimpleWeblog
python -m venv env
source env/bin/activate       # On Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver