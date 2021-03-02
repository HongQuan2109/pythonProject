from flask import Flask, template_rendered, redirect, url_for
from flask_login import UserMixin
from app import db, admin
app = Flask(__name__)

class User(db.Model, userMixin):
    __tablename__ = "user"
    id = Column(interger, primary_key)

@app.route("/")
def homepage():
    return "Hello!This is homepage <h1>Welcome user!!</h2>"

#
# @app.route("/admin")
# def admin():
#     return redirect(url_for("user", name='user_id'))





@app.route("/login", methods=["get", "post"])
def login_user():
    if request.method == 'POST':
        username = request.form["un"]
        password = request.form["pass"]
        if username == "admin" and password =="123":
            return template_rendered()

@app.route("/<name>")
def profile(name):
    return template_rendered("profile.html", name=name)


# @app.route('/user/<int:user_id>')
# def user(user_id):
#     return"<h2>Your user ID is %s</h2>" % user_id
#
#
# @app.route("/login", methods=["get", "post"])
# def login_admin():
#     return redirect("/admin")

if __name__ == "__main__":
    app.run(debug=True)
