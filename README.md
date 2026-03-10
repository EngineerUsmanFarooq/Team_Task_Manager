Team Task Flow 🚀

A professional, full-stack Task Management application built for collaboration. This project enables users to create teams, manage members, and track tasks with a clean, modern UI and a secure Django backend.

✨ Key Features

- Secure Authentication: Robust user registration and login with encrypted passwords.
- Team Management: Create teams and invite members by username.
- Collaborative Tasks: Assign tasks to specific teams and track progress.
- Role-Based Access: Specialized permissions where only team creators can manage team settings.
- Advanced Filtering: Search tasks by title or filter by specific teams.
- Responsive Design: A premium, card-based UI that works seamlessly on all devices.

🛠️ Tech Stack

Frontend
- React 18: Component-based architecture.
- Tailwind CSS v4: Professional styling and layout.
- Vite: Ultra-fast build tool and development server.
- Lucide React: High-quality SVG icons.
- Framer Motion: Smooth animations and transitions.

Backend
- Python / Django: High-level web framework.
- Django REST Framework (DRF): Scalable and consistent API architecture.
- PostgreSQL: Production-grade relational database.
- Gunicorn: High-performance WSGI HTTP Server.
- WhiteNoise: Efficient static file management.

🚀 Live Demo

Link: https://ttm-omega.vercel.app

🛠️ Local Setup & Dependencies

Prerequisites
- Python 3.10+
- Node.js 20+
- npm (comes with Node.js)

Backend Setup
1. Clone the repository:
   ```bash
   git clone <https://github.com/EngineerUsmanFarooq/Team_Task_Manager>
   cd Team_Task_Manager/backend
   ```
2. Create and Activate Virtual Environment:
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Mac/Linux:
   source venv/bin/activate
   ```
3. Install Python Dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *The requirements file includes: Django, Django REST Framework, django-cors-headers, dj-database-url, psycopg2-binary, whitenoise, and gunicorn.*

4. Initialize Database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Start Development Server:
   ```bash
   python manage.py runserver
   ```

Frontend Setup
1. **Navigate to the frontend folder:
   ```bash
   cd ../frontend
   ```
2. Install Node Dependencies:
   ```bash
   npm install
   ```
   *This installs: React, Vite, Tailwind CSS v4, Axios, Lucide React, and Framer Motion.*

3. Start the Development Server:
   ```bash
   npm run dev
   ```
4. Access the Application:
   Open [http://localhost:5173](http://localhost:5173) in your browser.

🔒 Security Practices

- Hashed Passwords: Never stored in plain text (uses Django's default PBKDF2).
- Session Management: Uses secure, HTTP-only cookies.
- CSRF Protection: Configured for cross-site API requests.
- Environment Variables: Sensitive keys and database URLs are managed via `.env` files.

📄 License

This project is licensed under the MIT License.
