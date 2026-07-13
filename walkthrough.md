# Walkthrough - Expense Tracker Application

This walkthrough outlines the implemented codebase structure for the **Expense Tracker Application** and guides you through setting it up locally and deploying it online with a tunnel.

## Completed Tasks

### 1. Backend Implementation (Django REST APIs)
- Created Django project directory structure with `core/` for configs and `api/` for models, views, and urls.
- Developed all **5 database schemas**: `User`, `Income`, `Expense`, `Category`, and `Budget` inside [models.py](file:///c:/Users/gorla/Desktop/projects/ExpenseTracker/Backend/api/models.py).
- Programmed all **20 CRUD endpoint views** inside [views.py](file:///c:/Users/gorla/Desktop/projects/ExpenseTracker/Backend/api/views.py) with `@csrf_exempt` decorators and CORS enabled.
- Established correct root-level mapping files [db.py](file:///c:/Users/gorla/Desktop/projects/ExpenseTracker/Backend/db.py), [views.py](file:///c:/Users/gorla/Desktop/projects/ExpenseTracker/Backend/views.py), and [urls.py](file:///c:/Users/gorla/Desktop/projects/ExpenseTracker/Backend/urls.py).

### 2. Frontend Development (HTML/CSS/JS)
- Designed a **premium glassmorphic styling grid system** inside [style.css](file:///c:/Users/gorla/Desktop/projects/ExpenseTracker/Frontend/style.css) with rich gradient buttons, active sidebar highlights, and clean dashboards.
- Programmed central Fetch API logic inside [script.js](file:///c:/Users/gorla/Desktop/projects/ExpenseTracker/Frontend/script.js) with cache-busting timestamp features and custom network/server error alerts.
- Built **all 8 requested pages** with modals and AJAX list updating:
  - `index.html` (Landing information portal)
  - `login.html` & `register.html` (Secure mock session login/registration)
  - `dashboard.html` (Overall savings, total metrics, and merged recent transaction list)
  - `income.html` & `expenses.html` (CRUD interfaces with category filter capability)
  - `categories.html` & `budget.html` (Category limits config & monthly saving planners with automatic Over/Under budget status calculation)

### 3. Setup Automation & Documentation
- Created a database migrator/seeder script [seed_db.py](file:///c:/Users/gorla/Desktop/projects/ExpenseTracker/Backend/seed_db.py) to automatically apply configurations and insert the sample "Rahul Sharma" testing data.
- Documented complete environment instructions inside [README.md](file:///c:/Users/gorla/Desktop/projects/ExpenseTracker/README.md).

---

## Guide: Running the Tunnel and Deploying (Vercel)

### Step 1: Run the Backend Database Seeder
Open a terminal in the `ExpenseTracker/Backend` directory and execute:
```powershell
pip install -r requirements.txt
python seed_db.py
```
*(This creates `db.sqlite3` and seeds the tables)*

### Step 2: Start the Django Server
```powershell
python manage.py runserver
```
*(Keep this terminal open and running)*

### Step 3: Run the Tunnel (Localtunnel)
Open a separate terminal window and run:
```powershell
npx localtunnel --port 8000 --local-host 127.0.0.1
```
Copy the generated URL (e.g. `https://xxxx.loca.lt`). **Do not close this terminal.**

### Step 4: Update Frontend URL
1. Open [script.js](file:///c:/Users/gorla/Desktop/projects/ExpenseTracker/Frontend/script.js).
2. Change the `API_BASE` variable on line 1 to your generated localtunnel URL.
3. Save the file.

### Step 5: Push to GitHub (Avoid Submodule Trap)
Navigate to the root directory `ExpenseTracker` in your Git terminal and run:
```powershell
git init
git add .
git commit -m "Initialize Expense Tracker Project"
git branch -M main
git remote add origin https://github.com/vasavi249/Expense-Tracker.git
git push -u origin main --force
```
*(Make sure to use a new/separate GitHub repository for this project to keep it clean!)*

### Step 6: Deploy & Bypassing the warning
1. On Vercel, connect this new repository.
2. In Vercel Project Settings, change **Root Directory** to `Frontend` and deploy.
3. Before loading the Vercel site, open your generated localtunnel link in your browser tab, enter the IP shown in the grey box, and click **Continue**.
4. Now, open your Vercel URL, and everything will connect and sync live!
