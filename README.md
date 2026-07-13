# Expense Tracker Application

An advanced digital system to manage personal and business budgets, category limits, income, and expenses with real-time statistics.

## Technology Stack
- **Frontend**: HTML5, CSS3, JavaScript (ES6), Fetch API
- **Backend**: Django (Function-Based Views, REST APIs)
- **Database**: SQLite (default configuration)

---

## Folder Structure
```text
ExpenseTracker/
│── Backend/
│     db.py
│     views.py
│     urls.py
│     manage.py
│     requirements.txt
│     seed_db.py
│     core/
│     api/
└── Frontend/
      index.html
      login.html
      register.html
      dashboard.html
      income.html
      expenses.html
      categories.html
      budget.html
      style.css
      script.js
```

---

## Setup & Execution Guide

### 1. Set Up the Backend
Navigate to the `Backend` directory:
```bash
cd Backend
```

Install the dependencies:
```bash
pip install -r requirements.txt
```

Run migrations and seed the database with sample data:
```bash
python seed_db.py
```

Start the Django REST server:
```bash
python manage.py runserver
```
The backend server will start on `http://127.0.0.1:8000/`.

---

### 2. Set Up the Frontend (Localtunnel)
To make your frontend (live on Vercel) talk to your local backend securely:

1. Start your local Django backend:
   ```bash
   python manage.py runserver
   ```
2. Open a new terminal and start a localtunnel forwarding to port `8000`:
   ```bash
   npx localtunnel --port 8000 --local-host 127.0.0.1
   ```
   *Take note of the URL generated (e.g. `https://xxxx.loca.lt`).*
3. Update `Frontend/script.js` line 1:
   ```javascript
   const API_BASE = 'https://xxxx.loca.lt'; // Replace with your generated link
   ```
4. Commit and push your code to your GitHub repository so Vercel can rebuild.
5. In your web browser, open the tunnel link (`https://xxxx.loca.lt`) directly in a tab, enter the IP shown on screen, and click **Continue**.
6. Access your Vercel frontend URL, and you can add users, log incomes, create budgets, and view reports live!

---

## API Endpoints (20 REST CRUD APIs)

### User Management
- `POST /users/add/` - Register a user profile
- `GET /users/` - View all user profiles
- `PUT /users/update/<id>/` - Update user details
- `DELETE /users/delete/<id>/` - Delete user

### Income Management
- `POST /income/add/` - Add an income entry
- `GET /income/` - Fetch all income history
- `PUT /income/update/<id>/` - Update income detail
- `DELETE /income/delete/<id>/` - Delete income record

### Expense Management
- `POST /expenses/add/` - Record an expense entry
- `GET /expenses/` - Fetch all expenses
- `PUT /expenses/update/<id>/` - Update expense details
- `DELETE /expenses/delete/<id>/` - Delete expense record

### Category Management
- `POST /categories/add/` - Add a category limit
- `GET /categories/` - Fetch all categories
- `PUT /categories/update/<id>/` - Update category details
- `DELETE /categories/delete/<id>/` - Delete category record

### Budget Management
- `POST /budgets/add/` - Add a monthly budget planner
- `GET /budgets/` - Fetch all budget plans
- `PUT /budgets/update/<id>/` - Update budget status
- `DELETE /budgets/delete/<id>/` - Delete budget plan
