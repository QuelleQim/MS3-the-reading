import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env
from datetime import datetime


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_reviews")
def get_reviews():
    reviews = list(mongo.db.reviews.find())
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "reviews.html", reviews=reviews, categories=categories)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    sort_by = request.form.get("sort_by")
    reviews = list(mongo.db.reviews.find({"$text": {"$search": query}}))
    categories = mongo.db.categories.find().sort("category_name", 1)

    def get_grade(review):
        return review.get('grade')

    def get_page_length(review):
        return review.get('page_length')

    if categories == "category_name":
        categories.find(key=get_categories, reverse=True)

    if sort_by == "grade_highest":
        reviews.sort(key=get_grade, reverse=True)
    if sort_by == "grade_lowest":
        reviews.sort(key=get_grade)
    if sort_by == "page_highest":
        reviews.sort(key=get_page_length, reverse=True)
    if sort_by == "page_lowest":
        reviews.sort(key=get_page_length)

    return render_template(
        "reviews.html", reviews=reviews, categories=categories)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            # Code for date in python was retrived from w3schools.com
            "member_since": datetime.today()
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {} :)".format(
                        request.form.get("username")))
                return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # retrive the session user's username from db
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    reviews = list(mongo.db.reviews.find({"created_by": user["username"]}))

    if session["user"]:
        return render_template(
                                "profile.html",
                                user=user,
                                username=username,
                                reviews=reviews)

    return redirect(url_for("login"))


@app.route("/delete_user/<user_id>")
def delete_user(user_id):
    # remove user account from database and session cookies
    mongo.db.users.remove({"_id": ObjectId(user_id)}),
    flash("Account Successfully Deleted"),
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        explicit_content = "on" if request.form.get(
            "explicit_content") else "off"
        review = {
            "book_name": request.form.get("book_name"),
            "author_name": request.form.get("author_name"),
            "category_name": request.form.get("category_name"),
            "book_language": request.form.get("book_language"),
            # integer converter retrived from
            # https://careerkarma.com/blog/python-string-to-int/
            "page_length": int(request.form.get("page_length")),
            "published_date": request.form.get("published_date"),
            "grade": int(request.form.get("grade")),
            "review_description": request.form.get("review_description"),
            "explicit_content": explicit_content,
            "created_by": session["user"]
        }
        mongo.db.reviews.insert_one(review)
        flash("Review Successfully Added!")
        return redirect(url_for("get_reviews"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_review.html", categories=categories)


@app.route("/single_review/<review_id>")
def single_review(review_id):
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    return render_template("full_review.html", review=review)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    if request.method == "POST":
        explicit_content = "on" if request.form.get(
            "explicit_content") else "off"
        submit = {
            "book_name": request.form.get("book_name"),
            "author_name": request.form.get("author_name"),
            "category_name": request.form.get("category_name"),
            "book_language": request.form.get("book_language"),
            # integer converter retrived from
            # https://careerkarma.com/blog/python-string-to-int/
            "page_length": int(request.form.get("page_length")),
            "published_date": request.form.get("published_date"),
            "grade": int(request.form.get("grade")),
            "review_description": request.form.get("review_description"),
            "explicit_content": explicit_content,
            "created_by": session["user"]
        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, submit)
        flash("Review Successfully Updated!")

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_review.html", review=review, categories=categories)


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    if "user" not in session:
        flash("Login to delete reviews")
        return redirect(url_for("get_reviews"))

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    if session["user"].lower() == review["created_by"].lower() or \
            session["user"].lower() == "admin":
        mongo.db.reviews.remove({"_id": ObjectId(review_id)})
        flash("Review Successfully Deleted")
        return redirect(url_for("get_reviews"))

    flash("Cannot delete other users reviews")
    return redirect(url_for("get_reviews"))


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))
    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


@app.route("/information")
def information():
    return render_template("information.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
