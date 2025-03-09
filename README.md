# **Django Blog**  

A fully functional blog web application built with Django, featuring user authentication, post creation, editing, deleting, and liking functionality.

## **Features**  
- User authentication (Login, Register, Logout)  
- Create, update, and delete blog posts  
- Like and unlike blog posts  
- Responsive UI using Bootstrap  
- TinyMCE editor for rich text content  

## **Installation**  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/Django-Blog.git
   cd Django-Blog
   ```

2. **Create and activate a virtual environment**  
   ```bash
   python -m venv env
   source env/bin/activate  # On macOS/Linux
   env\Scripts\activate     # On Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**  
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (optional, for admin access)  
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**  
   ```bash
   python manage.py runserver
   ```

7. Open **http://127.0.0.1:8000/** in your browser.

## **Usage**  
- Register a new user or log in with an existing account.  
- Create blog posts with a title, content, and optional formatting.  
- Edit or delete your own posts.  
- Like/unlike posts.  
- Admin panel available at `/admin`.  

## **Technologies Used**  
- **Django** (Python Web Framework)  
- **Bootstrap** (Frontend Styling)  
- **TinyMCE** (Rich Text Editor)  
- **SQLite** (Default Django Database)  

## **License**  
This project is open-source and available under the **MIT License**.

---

Replace `your-username` in the clone command with your actual GitHub username. Let me know if you want any modifications! 🚀
