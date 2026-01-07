📝 Django To‑Do Web Application

A full‑featured To‑Do web application built using **Django**, featuring authentication, task management, priorities, due dates, search & filters, statistics dashboard, and secure password reset via email.



🚀 Setup & Installation Steps

Follow these steps in order after cloning the repository.

 1️⃣ Clone the Repository

```bash
git clone <your-github-repo-url>
cd task_manager
```

2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
```

Activate:

* macOS / Linux

```bash
source venv/bin/activate
```

* Windows

```bash
venv\Scripts\activate
```

3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

4️⃣ Environment Variables Setup (IMPORTANT 🔐)

This project uses environment variables for security.

🔑 Required Variables

Add these to your `.bash_profile`, `.zshrc`, or `.env` file:

```bash
export DJANGO_SECRET_KEY="your-django-secret-key"
export EMAIL_USER="your-email@gmail.com"
export EMAIL_PASS="your-gmail-app-password"
```

Reload terminal:

```bash
source ~/.bash_profile
```

5️⃣ Gmail App Password (For Password Reset Emails)

Google does not allow normal passwords for apps.

#Steps:

1. Go to Google Account → Security
2. Enable 2‑Step Verification
3. Open App Passwords
4. Generate password for Mail
5. Copy and use it as `EMAIL_PASS`

📌 Official Link:
 [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)


6️⃣ Database Setup (Migrations)

Run these commands after models are ready:

```bash
python manage.py makemigrations
python manage.py migrate
```

7️⃣ Create Superuser (Admin Access)

```bash
python manage.py createsuperuser
```

Then access admin panel:

```
http://127.0.0.1:8000/admin/
```

8️⃣ Run Development Server

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

# Features

* User Authentication (Login / Register)
* Task CRUD Operations
* Due Dates & Priority Levels
* Search, Filter & Sorting
* Dashboard Statistics
* Email Password Reset (Secure)
* Environment‑based Secrets

# Tech Stack

* Frontend : HTML , CSS , Bootstrap 5 (for responsive UI )
* Backend : Python
* Framework : Django
* Database : SQLite, Django ORM 


#👤 Author

**Mahi Kalavadia**



⭐ If you like this project, give it a star on GitHub!
