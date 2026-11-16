
from flask import Flask, render_template, request, session, redirect, url_for
from database import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

# Create Flask application
app = Flask(__name__)
app.secret_key = "my-secret-key"

#print(app)


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        password_hash = generate_password_hash(password)

        connection = get_db_connection()

        try:
            connection.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, password_hash)
            )

            connection.commit()
            return "Registration successful!"

        except sqlite3.IntegrityError:
            return "Username already exists!"

        finally:
            connection.close()

    return render_template("register.html")

@app.route("/login" , methods=["GET","POST"])
def login():
    if(request.method == "POST"):
        username = request.form["username"]
        password = request.form["password"]
        
        connection = get_db_connection()

        try:
            user = connection.execute(
                    "SELECT username, password_hash FROM users WHERE username = ?",
                    (username,)
                ).fetchone()

            if user and check_password_hash(user["password_hash"], password):
                session["username"] = username
                return redirect(url_for("dashboard"))

            else:
                return "Invalid username or password!"

        finally:
            connection.close()


    return render_template("login.html")

@app.route("/dashboard")
def dashboard():

    if "username" in session:
        return render_template(
            "dashboard.html",
            username=session["username"]
        )

    return redirect(url_for("login"))
@app.route("/logout")
def logout():

    session.pop("username", None)

    return redirect(url_for("login"))
# Create the home page
@app.route("/")
def home():
    return render_template("home.html")

# Create another page
@app.route("/about")
def about():
    return "This application is developed using Python and Flask."

print(__name__)
# Start the Flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
