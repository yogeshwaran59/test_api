from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

# -------------------------------
# Fetch functions
# -------------------------------
def fetch_posts():
    return requests.get("https://jsonplaceholder.typicode.com/posts", timeout=5).json()

def fetch_comments():
    return requests.get("https://jsonplaceholder.typicode.com/comments", timeout=5).json()

def fetch_albums():
    return requests.get("https://jsonplaceholder.typicode.com/albums", timeout=5).json()


# -------------------------------
# Home route (loads index.html)
# -------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -------------------------------
# API routes (return JSON)
# -------------------------------
@app.route("/posts")
def posts():
    return jsonify(fetch_posts())


@app.route("/comments")
def comments():
    return jsonify(fetch_comments())


@app.route("/albums")
def albums():
    return jsonify(fetch_albums())


if __name__ == "__main__":
    app.run(debug=True)