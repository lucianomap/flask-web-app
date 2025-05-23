# 🌶 Simple Flask Web App

This is a simple web application built with [Flask](https://flask.palletsprojects.com/), designed to demonstrate the basic structure and functionality of a Flask project. 

It includes a simple API call and route handling.

---

## 🚀 Features

- 💻 API call using a JavaScript endpoint.
- 🧭 Route management via `views.py`
  - `/`: Home page. Contains a fetch button to interact with the data.
  - `/profile`: For testing queries like NAME and AGE.
      Usage: `/profile?name=NAME&age=AGE` should display a sample formatted sentence.
  - `/json`: Retrieves json data using jsonify.
  - `/data`: Shows data fetched by the button in the home page.
  - `/go-to-home`: Redirects user to home (`/`) page.

---
## 🗂️ Project Structure

- `app.py`: Initializes the Flask application.
- `views.py`: Contains route definitions and view functions.
- `templates/`: Directory for HTML templates.
- `static/`: Directory containing `.js` files used by the HTML templates.
- `requirements.txt`: Lists Python dependencies required to run the app.

---

## 🛠️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/lucianomap/flask-web-app.git
cd flask-web-app
```

2. Create a virtual environment (optional) 

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the dependencies with:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the API

You can start the server using `flask`:

```bash
flask run -p 8000 --reload
```
By default, the application will be accessible at http://127.0.0.1:5000, but this was changed to port 8000 to test Port Fowarding.

---

## 📄 License
This project is open source and available under the MIT License.
