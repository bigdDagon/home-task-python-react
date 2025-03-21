# Simple Blogging Platform

A full-stack blogging application built with **React** (frontend) and **Flask** (backend), featuring CRUD operations, data validation, and security best practices.

---

## Project Structure

blog-app/
├── backend/                # Flask backend
│   ├── venv/              # Python virtual environment
│   ├── app.py             # Main Flask application
│   ├── config.py          # Configuration settings
│   ├── requirements.txt   # Backend dependencies
│   ├── blog.db            # SQLite database (auto-generated)
│   ├── models.py          # Database models
│   ├── routes.py          # API route definitions
│   ├── static/            # Static files (if any)
│   ├── templates/         # HTML templates (if needed)
│   └── tests/             # Backend test cases
│
├── frontend/               # React frontend
│   ├── public/            # Static assets
│   ├── src/               # React source code
│   │   ├── components/    # Reusable UI components
│   │   ├── pages/         # Application pages
│   │   ├── services/      # API service handlers
│   │   ├── styles/        # CSS and styling files
│   │   ├── App.js         # Root component
│   │   ├── index.js       # Entry point
│   ├── package.json       # Frontend dependencies
│   ├── .env               # Environment variables
│   └── tests/             # Frontend test cases
│
├── README.md               # Project documentation (this file)
└── .gitignore              # Files to ignore in version control
```

---

## Features
- **Create, Read, Update, Delete (CRUD)** blog posts
- **RESTful API** with Flask backend
- **SQLite database** for data storage
- **Security Best Practices**: SQL Injection Prevention, XSS Protection, CORS
- **Responsive UI** built with React
- **Dockerized Deployment** for scalability

---

## Installation
### Prerequisites
- **Node.js** (v14 or higher)
- **Python** (v3.8 or higher)
- **npm** (v6 or higher)
- **pip** (v21 or higher)

### Backend Setup
```bash
cd backend
python -m venv venv
# Activate the virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
pip install -r requirements.txt
python app.py
```
The backend will start at `http://localhost:5000`.

### Frontend Setup
```bash
cd frontend
npm install
npm start
```
The frontend will start at `http://localhost:3000`.

---

## API Endpoints
| Method | Endpoint           | Description              |
|--------|-------------------|--------------------------|
| POST   | /api/posts       | Create a new blog post   |
| GET    | /api/posts       | Retrieve all blog posts  |
| GET    | /api/posts/<id>  | Retrieve a specific post |
| PUT    | /api/posts/<id>  | Update a blog post       |
| DELETE | /api/posts/<id>  | Delete a blog post       |

Example API Request:
```bash
curl -X POST http://localhost:5000/api/posts \
  -H "Content-Type: application/json" \
  -d '{"title": "My First Post", "content": "Hello, world!"}'
```

---

## Database Management
The SQLite database (`blog.db`) is automatically created in the backend folder when you run the Flask server for the first time.

### Viewing the Database
Using DB Browser for SQLite:
1. Download **DB Browser for SQLite**.
2. Open `backend/blog.db`.
3. Browse the `post` table to see your blog posts.

Using Command Line:
```bash
sqlite3 backend/blog.db
sqlite> .tables          # List all tables
sqlite> SELECT * FROM post;  # View all blog posts
```

---

## Security Features
- **SQL Injection Prevention**: Uses SQLAlchemy ORM for parameterized queries.
- **XSS Protection**: Sanitizes user input with Bleach.
- **CORS**: Enabled for safe communication between frontend and backend.

---

## Troubleshooting
### Database not created:
Run the following commands in the backend folder:
```bash
flask shell
>>> from app import db
>>> db.create_all()
```

### Dependency errors:
- Reinstall dependencies using `pip install -r requirements.txt` (backend) or `npm install` (frontend).

### CORS issues:
Ensure `Flask-CORS` is installed and configured in `app.py`.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.


## Acknowledgments
- Flask Documentation
- React Documentation
- SQLAlchemy ORM
- Bleach Library

