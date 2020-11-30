from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/<username>/<int:post_id>")
def hello_world(username=None, post_id=None):
    return render_template("index.html", name=username, post_id=post_id)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/blog")
def blog():
    return "This is my thought on blogs"


@app.route("/blog/2020/dog")
def blog_dog():
    return "This is a blog about dogs"
